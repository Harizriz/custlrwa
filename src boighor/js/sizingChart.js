// Code written by Gerald
// adjustable set sizing from sizing charts for men and womens tops and bottoms
var men_tops = [
    {
        "uk": "34",
        "us": "34",
        "eu": "44",
        "intl": "XS",
        "tops": {
            "chest": "35.5",
            "waist": "31",
            "hip": "35.75",
            "arm": "32.5"
        }
    },
    {
        "uk": "36",
        "us": "36",
        "eu": "46",
        "intl": "S",
        "tops": {
            "chest": "37",
            "waist": "32.5",
            "hip": "37.5",
            "arm": "33"
        }
    },
    {
        "uk": "38",
        "us": "38",
        "eu": "48",
        "intl": "M",
        "tops": {
            "chest": "38.5",
            "waist": "34",
            "hip": "39",
            "arm": "33.5"
        }
    },
    {
        "uk": "40",
        "us": "40",
        "eu": "50",
        "intl": "L",
        "tops": {
            "chest": "40.25",
            "waist": "35.5",
            "hip": "40.5",
            "arm": "34.25"
        }
    },
    {
        "uk": "42",
        "us": "42",
        "eu": "52",
        "intl": "XL",
        "tops": {
            "chest": "41.75",
            "waist": "37.25",
            "hip": "42.75",
            "arm": "34.5"
        }
    },
    {
        "uk": "44",
        "us": "44",
        "eu": "54",
        "intl": "XXL",
        "tops": {
            "chest": "43.25",
            "waist": "38.75",
            "hip": "43.75",
            "arm": "35"
        }
    },
    {
        "uk": "46",
        "us": "46",
        "eu": "56",
        "intl": "XXXL",
        "tops": {
            "chest": "44.75",
            "waist": "40.25",
            "hip": "45.25",
            "arm": "35.5"
        }
    }
];

var men_bottoms = [
    {
        "uk": "28",
        "us": "28",
        "eu": "44",
        "intl": "XS",
        "bottoms": {
            "waist": "31",
            "hip": "35.75",
            "inseam": "33.5"
        }
    },
    {
        "uk": "32",
        "us": "32",
        "eu": "46",
        "intl": "S",
        "bottoms": {
            "waist": "32.5",
            "hip": "37.5",
            "inseam": "33.5"
        }
    },
    {
        "uk": "34",
        "us": "34",
        "eu": "48",
        "intl": "M",
        "bottoms": {
            "waist": "34",
            "hip": "39",
            "inseam": "33.5"
        }
    },
    {
        "uk": "36",
        "us": "36",
        "eu": "50",
        "intl": "L",
        "bottoms": {
            "waist": "35.5",
            "hip": "40.5",
            "inseam": "33.5"
        }
    },
    {
        "uk": "38",
        "us": "38",
        "eu": "52",
        "intl": "XL",
        "bottoms": {
            "waist": "37.25",
            "hip": "42.25",
            "inseam": "33.5"
        }
    },
    {
        "uk": "40",
        "us": "40",
        "eu": "54",
        "intl": "XXL",
        "bottoms": {
            "waist": "38.75",
            "hip": "43.75",
            "inseam": "33.5"
        }
    },
    {
        "uk": "42",
        "us": "42",
        "eu": "56",
        "intl": "XXXL",
        "bottoms": {
            "waist": "40.25",
            "hip": "45.25",
            "inseam": "33.5"
        }
    }
];

var women_tops = [
    {
        "uk": "2",
        "us": "00",
        "eu": "30",
        "intl": "XS",
        "tops":{
            "chest": "30",
            "waist": "23",
            "hip": "33",
            "arm": "30"
        }
    },
    {
        "uk": "4",
        "us": "0",
        "eu": "32",
        "intl": "XS",
        "tops":{
            "chest": "31",
            "waist": "24",
            "hip": "34",
            "arm": "30"
        }
    },
    {
        "uk": "6",
        "us": "2",
        "eu": "34",
        "intl": "S",
        "tops":{
            "chest": "32",
            "waist": "25",
            "hip": "35",
            "arm": "30.75"
        }
    },
    {
        "uk": "8",
        "us": "4",
        "eu": "36",
        "intl": "S",
        "tops":{
            "chest": "33",
            "waist": "26",
            "hip": "36",
            "arm": "30.75"
        }
    },
    {
        "uk": "10",
        "us": "6",
        "eu": "38",
        "intl": "M",
        "tops":{
            "chest": "35",
            "waist": "28",
            "hip": "38",
            "arm": "31.25"
        }
    },
    {
        "uk": "12",
        "us": "8",
        "eu": "40",
        "intl": "M",
        "tops":{
            "chest": "37",
            "waist": "30",
            "hip": "40",
            "arm": "31.25"
        }
    },
    {
        "uk": "14",
        "us": "10",
        "eu": "42",
        "intl": "L",
        "tops":{
            "chest": "39",
            "waist": "32",
            "hip": "42",
            "arm": "31.5"
        }
    }
];

var women_bottoms = [
    {
        "uk": "2",
        "us": "00",
        "eu": "30",
        "intl": "XS",
        "bottoms":{
            "waist": "30.75",
            "hip": "35.5",
            "inseam": "32.25"
        }
    },
    {
        "uk": "4",
        "us": "0",
        "eu": "32",
        "intl": "XS",
        "bottoms":{
            "waist": "30.75",
            "hip": "35.5",
            "inseam": "32.25"
        }
    },
    {
        "uk": "6",
        "us": "2",
        "eu": "34",
        "intl": "S",
        "bottoms":{
            "waist": "32.25",
            "hip": "37",
            "inseam": "32.5"
        }
    },
    {
        "uk": "8",
        "us": "4",
        "eu": "36",
        "intl": "S",
        "bottoms":{
            "waist": "32.25",
            "hip": "37",
            "inseam": "32.5"
        }
    },
    {
        "uk": "10",
        "us": "6",
        "eu": "38",
        "intl": "M",
        "bottoms":{
            "waist": "33.75",
            "hip": "38.5",
            "inseam": "33"
        }
    },
    {
        "uk": "12",
        "us": "8",
        "eu": "40",
        "intl": "M",
        "bottoms":{
            "waist": "33.75",
            "hip": "38.5",
            "inseam": "33"
        }
    },
    {
        "uk": "14",
        "us": "10",
        "eu": "42",
        "intl": "L",
        "bottoms":{
            "waist": "35.5",
            "hip": "40",
            "inseam": "33.5"
        }
    }
];

// detects sizing type and whether a product is a top or bottom
function sizingDetection(sizeType, gender, category){ 
    var sizingType = '';
    if (gender == 'Men'){
        if (sizeType == "UK"){
            if (category == 'tops'){
                sizingType = 'us_uk_men_tops'; //same sizing for both
            }
            else{
                sizingType = 'us_uk_men_bottoms';
            }
        }
        else if (sizeType == "EU") {
            if (category == 'tops'){
                sizingType = 'eu_men_tops';
            }
            else{
                sizingType = 'eu_men_bottoms'
            }
        }
        else if (sizeType == "International"){
            if(category == 'tops'){
                sizingType = 'intl_men_tops';    
            }
            else{
                sizingType = 'intl_men_bottoms';
            }
        }
        else{
            sizingType = 'notype'
        }       
    }
    else if (gender === 'Women'){ //add for bottoms
        if (sizeType == "UK"){
            if (category == 'tops'){
                sizingType = 'us_uk_women_tops'; //same sizing for both
            }
            else{
                sizingType = 'us_uk_women_bottoms';
            }
        }
        else if (sizeType == "EU") {
            if (category == 'tops'){
                sizingType = 'eu_women_tops';
            }
            else{
                sizingType = 'eu_women_bottoms'
            }
        }
        else if (sizeType == "International"){
            if(category == 'tops'){
                sizingType = 'intl_women_tops';    
            }
            else{
                sizingType = 'intl_women_bottoms';
            }
        }
        else{
            sizingType = 'notype'
        } 
    }
    else { //Kids
        sizingType = 'notype'
    }
    return sizingType;
}

// generates a converted size based on variables
function sizingList(sizing_original, sizeType, gender, category){
    var sizing_list = []
    var sizingType = sizingDetection(sizeType, gender, category)
    var i=0, j=0;
    switch(sizingType){
        case 'us_uk_men_tops':
            //for loop to look through the original sizing list, match with sizes on the input sizing for this function, then += to sizing_list
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<men_tops.length; j++){
                    if (sizing_original[i].sizing == men_tops[j].uk || sizing_original[i].sizing == men_tops[j].us){
                        sizing_list.push(men_tops[j]);
                    };
                };
            };
            break;
        case 'us_uk_men_bottoms':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<men_bottoms.length; j++){
                    if (sizing_original[i].sizing == men_bottoms[j].uk || sizing_original[i].sizing == men_bottoms[j].us){
                        sizing_list.push(men_bottoms[j]);
                    };
                };
            };
            break;
        case 'eu_men_tops':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<men_tops.length; j++){
                    if (sizing_original[i].sizing == men_tops[j].eu){
                        sizing_list.push(men_tops[j]);
                    };
                };
            };
            break;
        case 'eu_men_bottoms':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<men_bottoms.length; j++){
                    if (sizing_original[i].sizing == men_bottoms[j].eu){
                        sizing_list.push(men_bottoms[j]);
                    };
                };
            };
            break;
        case 'intl_men_tops':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<men_tops.length; j++){
                    if (sizing_original[i].sizing == men_tops[j].intl){
                        sizing_list.push(men_tops[j]);
                    };
                };
            };
            break;
        case 'intl_men_bottoms':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<men_bottoms.length; j++){
                    if (sizing_original[i].sizing == men_bottoms[j].intl){
                        sizing_list.push(men_bottoms[j]);
                    };
                };
            };
            break;
        case 'us_uk_women_tops':
            //for loop to look through the original sizing list, match with sizes on the input sizing for this function, then += to sizing_list
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<women_tops.length; j++){
                    if (sizing_original[i].sizing == women_tops[j].uk || sizing_original[i].sizing == women_tops[j].us){
                        sizing_list.push(women_tops[j]);
                    };
                };
            };
            break;
        case 'us_uk_women_bottoms':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<women_bottoms.length; j++){
                    if (sizing_original[i].sizing == women_bottoms[j].uk || sizing_original[i].sizing == women_bottoms[j].us){
                        sizing_list.push(women_bottoms[j]);
                    };
                };
            };
            break;
        case 'eu_women_tops':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<women_tops.length; j++){
                    if (sizing_original[i].sizing == women_tops[j].eu){
                        sizing_list.push(women_tops[j]);
                    };
                };
            };
            break;
        case 'eu_women_bottoms':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<women_bottoms.length; j++){
                    if (sizing_original[i].sizing == women_bottoms[j].eu){
                        sizing_list.push(women_bottoms[j]);
                    };
                };
            };
            break;
        case 'intl_women_tops':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<women_tops.length; j++){
                    if (sizing_original[i].sizing == women_tops[j].intl){
                        sizing_list.push(women_tops[j]);
                    };
                };
            };
            break;
        case 'intl_women_bottoms':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<women_bottoms.length; j++){
                    if (sizing_original[i].sizing == women_bottoms[j].intl){
                        sizing_list.push(women_bottoms[j]);
                    };
                };
            };
            break;
        case 'notype':
            for (i=0; i<sizing_original.length; i++){
                var noTypeSizing = {
                    "uk": "0",
                    "us": "0",
                    "eu": "0",
                    "intl": "0"
                }
                noTypeSizing.uk = sizing_original[i].sizing;
                noTypeSizing.us = sizing_original[i].sizing;
                noTypeSizing.eu = sizing_original[i].sizing;
                noTypeSizing.intl = sizing_original[i].sizing;

                sizing_list.push(noTypeSizing);
            };
            break;
        default:
            for (i=0; i<sizing_original.length; i++){
                var noTypeSizing = {
                    "uk": "0",
                    "us": "0",
                    "eu": "0",
                    "intl": "0"
                }
                noTypeSizing.uk = sizing_original[i].sizing;
                noTypeSizing.us = sizing_original[i].sizing;
                noTypeSizing.eu = sizing_original[i].sizing;
                noTypeSizing.intl = sizing_original[i].sizing;

                sizing_list.push(noTypeSizing);
            }

    }
    return sizing_list
}

// matches custom sizes with multiple if-else statements to specifically categorize clothing item and gender
function sizing_match(user_sizing, size, type, gender){ // user measurements, available sizes(sizing_chart), type(top/bottom), gender
    if (type == 'tops'){
        return top_match(user_sizing, size, gender);
    }
    else if (type == 'bottoms'){ //bottoms
        return bottom_match(user_sizing, size, gender);
    }
    else{ // null
        return 'notype'; // have if statement to handle in pages
    }
};

function top_match(user, size, gender){
    if (gender == 'Men'){
        return tops_men(user, size);
    }
    else{
        return tops_women(user, size);
    }
}

function bottom_match(user, size, gender){
    if (gender == 'Men'){
        return bottoms_men(user, size);
    }
    else{
        return bottoms_women(user, size);
    }
}

function compare(first, second){
    //comparison and sort, higher score == better

    var comparison = 0;
    if (first.score > second.score){
        comparison = -1;
    } else if (first.score < second.score){
        comparison = 1;
    } else if (first.original.uk > second.original.uk){
        comparison = -1;
    } else if (first.original.uk < second.original.uk){
        comparison = 1;
    };
    return comparison;
};

function tops_men(user, size){
    var scores = [];  //'score' given at the end. best(highest) score is most reccomended size.
    //user gives all sizes in this format
    /*
    { "chest": "41"
    , "waist": "34"
    , "hip": "40"
    , "arm": "33"
    }
    */
    //original sizes are in this format
    /*
    {
        "uk": "46",
        "us": "46",
        "eu": "56",
        "intl": "XXXL",
        "tops": {
            "chest": "44.75",
            "waist": "40.25",
            "hip": "45.25",
            "arm": "35.5"
        }
    }
    */
    //compare and give a 'score' for all the available sizes
    for (i=0; i < size.length; i++){
        //each part of the body should have some weightage
        //these numbers are not 100% final, could change as time goes on, this is just a rough idea for implementation right now
        var sizing = size[i].tops;
        var score = 0;

        var chest = (user.chest - parseFloat(sizing.chest));
        if (chest <= 0 && chest >= -0.5){
            score += 0.25;
        };

        var waist = (user.waist - parseFloat(sizing.waist));
        if (waist <= 0 && waist >= -0.75){
            score += 0.35;
        };

        var hip = (user.hip - parseFloat(sizing.hip));
        if (hip <= 0 && hip >= -0.65){
            score += 0.25;
        };

        var arm = (user.arm - parseFloat(sizing.arm));
        if (arm <= 0 && arm >= -0.45){
            score += 0.15;
        };
        
        //use the different weighted scores now to get the final score
        var original = {
            "uk": size[i].uk,
            "us": size[i].us,
            "eu": size[i].eu,
            "intl": size[i].intl
        };
    
        score *=100;
        scores.push({"score": score, "original": original});
        
    }
    scores = scores.sort(compare);
    localStorage.setItem('best_mens_top', JSON.stringify(scores[0].original)); //best size in general, this will be sent to backend
    return scores; //returns list of sizing with score, unused if in search.
}

function tops_women(user, size){
    var scores = [];  //'score' given at the end. best(highest) score is most reccomended size.
    //user gives all sizes in this format
    /*
    { "chest": "30"
    , "waist": "23"
    , "hip": "33"
    , "arm": "30"
    }
    */
    //original sizes are in this format
    /*
    {
        "uk": "2",
        "us": "00",
        "eu": "30",
        "intl": "XS",
        "tops":{
            "chest": "30",
            "waist": "23",
            "hip": "33",
            "arm": "30"
        }
    }
    */
    //compare and give a 'score' for all the available sizes
    for (i=0; i < size.length; i++){
        //each part of the body should have some weightage
        //these numbers are not 100% final, could change as time goes on, this is just a rough idea for implementation right now
        var sizing = size[i].tops;
        var score = 0;

        var chest = (user.chest - parseFloat(sizing.chest));
        if (chest <= 0 && chest >= -0.5){
            score += 0.3;
        };

        var waist = (user.waist - parseFloat(sizing.waist));
        if (waist <= 0 && waist >= -0.75){
            score += 0.3;
        };

        var hip = (user.hip - parseFloat(sizing.hip));
        if (hip <= 0 && hip >= -0.65){
            score += 0.3;
        };

        var arm = (user.arm - parseFloat(sizing.arm));
        if (arm <= 0 && arm >= -0.45){
            score += 0.1;
        };
        
        //use the different weighted scores now to get the final score
        var original = {
            "uk": size[i].uk,
            "us": size[i].us,
            "eu": size[i].eu,
            "intl": size[i].intl
        };
        
        score *=100;
        scores.push({"score": score, "original": original});
    }
    scores = scores.sort(compare);
    localStorage.setItem('best_womens_top', JSON.stringify(scores[0].original)); //best size in general, this will be sent to backend
    return scores; //returns list of sizing with score, unused if in search.
}

function bottoms_men(user, size){
    var scores = [];  //'score' given at the end. best(highest) score is most reccomended size.
    //user gives all sizes in this format
    /*
    { "waist": "31"
    , "hip": "35.75"
    , "inseam": "33.5"
    }
    */
    //original sizes are in this format
    /*
    {
        "uk": "28",
        "us": "28",
        "eu": "44",
        "intl": "XS",
        "bottoms": {
            "waist": "31",
            "hip": "35.75",
            "inseam": "33.5"
        }
    }
    */
    //compare and give a 'score' for all the available sizes
    for (i=0; i < size.length; i++){
        //each part of the body should have some weightage
        //these numbers are not 100% final, could change as time goes on, this is just a rough idea for implementation right now
        var sizing = size[i].bottoms;
        var score = 0;

        var waist = (user.waist - parseFloat(sizing.waist));
        if (waist <= 0 && waist >= -0.5){
            score += 0.45;
        };

        var hip = (user.hip - parseFloat(sizing.hip));
        if (hip <= 0 && hip >= -0.5){
            score += 0.4;
        };

        var inseam = (user.inseam - parseFloat(sizing.inseam));
        if (inseam <= 0 && inseam >= -0.65){
            score += 0.15;
        };

        //use the different weighted scores now to get the final score
        var original = {
            "uk": size[i].uk,
            "us": size[i].us,
            "eu": size[i].eu,
            "intl": size[i].intl
        };
        
        score *=100;
        scores.push({"score": score, "original": original});
    }
    scores = scores.sort(compare);
    localStorage.setItem('best_mens_bottom', JSON.stringify(scores[0].original)); //best size in general, this will be sent to backend
    return scores; //returns list of sizing with score, unused if in search.
}

function bottoms_women(user, size){
    var scores = [];  //'score' given at the end. best(highest) score is most reccomended size.
    //user gives all sizes in this format
    /*
    { "waist": "31"
    , "hip": "35.75"
    , "inseam": "33.5"
    }
    */
    //original sizes are in this format
    /*
    {
        "uk": "28",
        "us": "28",
        "eu": "44",
        "intl": "XS",
        "bottoms": {
            "waist": "31",
            "hip": "35.75",
            "inseam": "33.5"
        }
    }
    */
    //compare and give a 'score' for all the available sizes
    for (i=0; i < size.length; i++){
        //each part of the body should have some weightage
        //these numbers are not 100% final, could change as time goes on, this is just a rough idea for implementation right now
        var sizing = size[i].bottoms;
        var score = 0;

        var waist = (user.waist - parseFloat(sizing.waist));
        if (waist <= 0 && waist >= -0.5){
            score += 0.45;
        };

        var hip = (user.hip - parseFloat(sizing.hip));
        if (hip <= 0 && hip >= -0.5){
            score += 0.4;
        };

        var inseam = (user.inseam - parseFloat(sizing.inseam));
        if (inseam <= 0 && inseam >= -0.65){
            score += 0.15;
        };

        //use the different weighted scores now to get the final score
        var original = {
            "uk": size[i].uk,
            "us": size[i].us,
            "eu": size[i].eu,
            "intl": size[i].intl
        };
        
        score *=100;
        scores.push({"score": score, "original": original});
    }
    scores = scores.sort(compare);
    localStorage.setItem('best_womens_bottom', JSON.stringify(scores[0].original)); //best size in general, this will be sent to backend
    return scores; //returns list of sizing with score, unused if in search.
}