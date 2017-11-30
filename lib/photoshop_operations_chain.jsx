function crop(img, paramsList){
    //get parameters
    var newWidth = paramsList['new_w'];
    var newHeight = paramsList['new_h'];
    var offX = paramsList['off_x'];
    var offY = paramsList['off_y'];
    
    //transform parameters
    var mL = offX;
    var mT = offY;
    var mR = mL + newWidth;
    var mB = mT + newHeight;

    var bounds = [mL, mT, mR, mB];

    img.crop(bounds);
    
    return img
}

function rotate(img, paramsList){
    //get parameters
    var angle = paramsList['angle'];
    
    //transform parameters
    var r = 0.5 * Math.min(doc.width, doc.height);
    var l = r / Math.sqrt(2);
    var offX = doc.width/2 - l;
    var offY= doc.height/2 -l;

    var originalWidth = doc.width;
    var originalHeight = doc.height;

    img.rotateCanvas(angle);
    img.resizeCanvas(originalWidth, originalHeight);
    var bounds = [offX, offY, offX + 2*l, offY + 2*l];

    img.crop(bounds);
    
    return img
}

function flip(img, paramsList){
    //get parameters        
    if (paramsList['orientation'] === "horizontal"){
    var orientation = Direction.HORIZONTAL;
    } else {
            var orientation = Direction.VERTICAL;
    }

    img.flipCanvas(orientation);

    return img
}

function scale(img, paramsList){
    //get parameters
    var factor = paramsList['factor'];
    
    if (paramsList['interpolation'] === "linear"){
    var interpolation = ResampleMethod.BILINEAR;
    }
    if (paramsList['interpolation'] === "cubic"){
            var interpolation = ResampleMethod.BICUBIC;
    }
    
    var width = img.width;
    var height = img.height;
    img.resizeImage (Math.floor(width * factor), Math.floor(height * factor), null, interpolation);
    
   return img
}

function makeEllipse(left, top, right, bottom, antialias){
    
    var circleSelection = charIDToTypeID( "setd" );
    var descriptor = new ActionDescriptor();
    var id71 = charIDToTypeID( "null" );
    var ref5 = new ActionReference();
    var id72 = charIDToTypeID( "Chnl" );
    var id73 = charIDToTypeID( "fsel" );
    ref5.putProperty( id72, id73 );
    descriptor.putReference( id71, ref5 );
    var id74 = charIDToTypeID( "T   " );
    var desc12 = new ActionDescriptor();

    var top1 = charIDToTypeID( "Top " );
    var top2 = charIDToTypeID( "#Pxl" );
    desc12.putUnitDouble( top1, top2, top );

    var left1 = charIDToTypeID( "Left" );
    var left2 = charIDToTypeID( "#Pxl" );
    desc12.putUnitDouble( left1, left2, left );

    var bottom1 = charIDToTypeID( "Btom" );
    var bottom2 = charIDToTypeID( "#Pxl" );
    desc12.putUnitDouble( bottom1, bottom2, bottom );

    var right1 = charIDToTypeID( "Rght" );
    var right2 = charIDToTypeID( "#Pxl" );
    desc12.putUnitDouble( right1, right2, right );

    var id83 = charIDToTypeID( "Elps" );
    descriptor.putObject( id74, id83, desc12 );
    var id84 = charIDToTypeID( "AntA" );
    descriptor.putBoolean( id84, antialias );

    executeAction( circleSelection, descriptor, DialogModes.NO );
}

function copyPaste(img, paramsList){
    //get parameters
    var shape = paramsList['shape'];
    var x = paramsList['x'];
    var y = paramsList['y'];
    var width = paramsList['width'];
    var height = paramsList['height'];
    var newX = paramsList['new_x'];
    var newY = paramsList['new_y'];
    if(paramsList['antialias'] === "true"){
    var antialias = true;
    } else {
        var antialias = false;
        }

    if (shape === "rectangle"){
        var selRegion = Array([x,y],
                                          [x, y+height],
                                          [x+width, y+height],
                                          [x+width, y]);
        img.selection.select(selRegion);
    }
    if (shape === "ellipse"){
        makeEllipse (x, y, x+width, y+height, antialias); 
    }

    img.selection.copy();

    var newSelRegion = Array([newX, newY],
                                      [newX, newY+height],
                                      [newX+width, newY+height],
                                      [newX+width, newY]);
                                      
    img.selection.select(newSelRegion);  
    img.paste ();
    img.flatten();
    
    return img
}

function blur(img, paramsList){
    img.activeLayer.applyBlur();
   
    return img
}

function motionBlur(img, paramsList){
    //get parameters
    var angle = paramsList['angle'];
    var radius = paramsList['radius'];
    
    img.activeLayer.applyMotionBlur(angle, radius);
    
    return img
}

function unsharp(img, paramsList){
    //get parameters
    var amount = paramsList['amount'];
    var radius = paramsList['radius'];
    var threshold = paramsList['threshold'];

    img.activeLayer.applyUnSharpMask(amount, radius, threshold);
    
    return img
}