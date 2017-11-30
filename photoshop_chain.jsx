#target photoshop
#include "lib/photoshop_operations_chain.jsx"

function save(doc, dstDir){
    saveOptions = new PNGSaveOptions(0, false);
    var dstName = dstDir + filename + "_" + ("000" + count).slice(-3) + "." + ext
    doc.saveAs(new File(dstName), saveOptions);
}

// set paths
var rootDir = "F:/home/nbonettini/projects/jt-parser/"; // set this to your root directory
var srcDir = rootDir + "test/img_src/";
var dstDir = rootDir + "test/img_dst/";
var paramsPath = rootDir + "test/parsed_journal_for_PS.json";

var withSaving = false  // intermediate results saving if true
var srcFolder = new Folder(srcDir);
var fileList = srcFolder.getFiles();

// read params from JSON
$.evalFile(rootDir + "/lib/json2.js")
var paramsFile = new File(paramsPath);
paramsFile.open('r');
var params = JSON.parse(paramsFile.read());
paramsFile.close();

// process images
for(j=0; j<fileList.length; j++){
        var file = fileList[j].fullName.substr(fileList[j].fullName.lastIndexOf("/") +1);
        var filename = file.split('.')[0];
        var ext = file.split('.')[1];
        var doc = app.open (fileList[j]);
        var count = 1;
        var saveOptions = new PNGSaveOptions();
        
        for(i=0; i<params.length; i++){
            if ('crop' in params[i]){
                crop(doc, params[i]['crop'])
                if (withSaving){
                    save(doc, dstDir)
                    count = count + 1;
                }
            }
            if ('rotate' in params[i]){
                rotate(doc, params[i]['rotate'])
                if (withSaving){
                    save(doc, dstDir)
                    count = count + 1;
                }
            }
            if ('flip' in params[i]){
                flip(doc, params[i]['flip'])
                if (withSaving){
                    save(doc, dstDir)
                    count = count + 1;
                }
            }
            if ('scale' in params[i]){
                scale(doc, params[i]['scale'])
                if (withSaving){
                    save(doc, dstDir)
                    count = count + 1;
                }
            }
            if ('copy_paste' in params[i]){
                doc = copyPaste(doc, params[i]['copy_paste']);
                if (withSaving){
                    save(doc, dstDir)
                    count = count + 1;
                }
            }
            if ('blur' in params[i]){
                blur(doc, params[i]['blur'])
                if (withSaving){
                    save(doc, dstDir)
                    count = count + 1;
                }
            }
            if ('motion_blur' in params[i]){
                motionBlur(doc, params[i]['motion_blur'])
                if (withSaving){
                    save(doc, dstDir)
                    count = count + 1;
                }
            }
            if ('unsharp' in params[i]){
                unsharp(doc, params[i]['unsharp'])
                if (withSaving){
                    save(doc, dstDir)
                    count = count + 1;
                }
            }
    }
    save (doc, dstDir);
    app.activeDocument.close (SaveOptions.DONOTSAVECHANGES);
}