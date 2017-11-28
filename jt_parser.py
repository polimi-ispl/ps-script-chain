import json
import sys

def chain_sort(chain, reorder_chain):
    if len(reorder_chain) == 0:
        reorder_chain.append(sorted(chain, key=lambda k: k['source'])[0])
    if len(reorder_chain) == len(chain):
        return
    reorder_chain.append([x for x in chain if x['source']==reorder_chain[-1]['target']][0])
    chain_sort(chain, reorder_chain)

def jt_parser(journal):
    # keep only interesting stuff
    clean = lambda x: {'op': x['op'], 'source': x['source'], 'target': x['target'], 'arguments': x['arguments']}
    chain = [clean(x) for x in journal['links']]
    
    # reconstruct original chain from chaos
    sorted_chain = []
    chain_sort(chain, sorted_chain)
    
    # operations' name translation
    translation = {
                        'GIMPCrop': 'crop',
                        'Flip': 'flip',
                        'Rotate': 'rotate',
                        'Scale': 'scale',
                        'GIMPCopyPaste': 'copy_paste',
                        'GIMPBlur': 'blur',
                        'MotionBlur': 'motion_blur',
                        'Unsharp': 'unsharp'
    }
    sorted_chain = [{translation[x['op']]: x['arguments']}
                    if x['op'] in translation.keys()
                    else {x['op']: x['arguments']} for x in sorted_chain]
    
    # clear undesired parameters
    undesired_parameters = ['dummy_argument', 'sigma']
    for x in chain:
        for key in x['arguments'].keys():
            if key in undesired_parameters:
                x['arguments'].pop(key)

    return json.dumps(sorted_chain, indent=4)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("The parser expects exactly 2 arguments")
    src = sys.argv[1]
    dst = sys.argv[2]
    with open(src, 'r') as f:
        journal = json.load(f)
    journal = jt_parser(journal)
    with open(dst, 'w') as f:
        f.write(journal)
