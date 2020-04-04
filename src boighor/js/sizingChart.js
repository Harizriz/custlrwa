var men_tops = [
    {
        "uk": "34",
        "us": "34",
        "eu": "44",
        "intl": "XS"
    },
    {
        "uk": "36",
        "us": "36",
        "eu": "46",
        "intl": "S"
    },
    {
        "uk": "38",
        "us": "38",
        "eu": "48",
        "intl": "M"
    },
    {
        "uk": "40",
        "us": "40",
        "eu": "50",
        "intl": "lL"
    },
    {
        "uk": "42",
        "us": "42",
        "eu": "52",
        "intl": "XL"
    },
    {
        "uk": "44",
        "us": "44",
        "eu": "54",
        "intl": "XXL"
    },
    {
        "uk": "46",
        "us": "46",
        "eu": "56",
        "intl": "XXXL"
    }
];

var men_trousers = [
    {
        "uk": "28",
        "us": "28",
        "eu": "44",
        "intl": "XS"
    },
    {
        "uk": "32",
        "us": "32",
        "eu": "46",
        "intl": "S"
    },
    {
        "uk": "34",
        "us": "34",
        "eu": "48",
        "intl": "M"
    },
    {
        "uk": "36",
        "us": "36",
        "eu": "50",
        "intl": "L"
    },
    {
        "uk": "38",
        "us": "38",
        "eu": "52",
        "intl": "XL"
    },
    {
        "uk": "40",
        "us": "40",
        "eu": "54",
        "intl": "XXL"
    },
    {
        "uk": "42",
        "us": "42",
        "eu": "56",
        "intl": "XXXL"
    }
];

var women = [
    {
        "uk": "2",
        "us": "00",
        "eu": "30",
        "intl": "XS"
    },
    {
        "uk": "4",
        "us": "0",
        "eu": "32",
        "intl": "XS"
    },
    {
        "uk": "6",
        "us": "2",
        "eu": "34",
        "intl": "S"
    },
    {
        "uk": "8",
        "us": "4",
        "eu": "36",
        "intl": "S"
    },
    {
        "uk": "10",
        "us": "6",
        "eu": "38",
        "intl": "M"
    },
    {
        "uk": "12",
        "us": "8",
        "eu": "40",
        "intl": "M"
    },
    {
        "uk": "14",
        "us": "10",
        "eu": "42",
        "intl": "L"
    }
];

var noTypeSizing = {
    "uk": "0",
    "us": "0",
    "eu": "0",
    "intl": "0"
}


function sizingDetection(sizeType, gender, category){ 
    var sizingType = '';
    if (gender == 'Men'){
        if (sizeType == "UK"){
            if (category == 'tops'){
                sizingType = 'us_uk_men_tops'; //same sizing for both
            }
            else{
                sizingType = 'us_uk_men_trousers';
            }
        }
        else if (sizeType == "EU") {
            if (category == 'tops'){
                sizingType = 'eu_men_tops';
            }
            else{
                sizingType = 'eu_men_trousers'
            }
        }
        else if (sizeType == "International"){
            if(category == 'tops'){
                sizingType = 'intl_men_tops';    
            }
            else{
                sizingType = 'intl_men_trousers';
            }
        }
        else{
            sizingType = 'notype'
        }       
    }
    else if (gender === 'Women'){ //women's tops and trousers are the same
        if (sizeType == "UK"){
            sizingType = 'uk_women'; //same sizing for both
        }
        else if(sizeType == "US"){
                sizingType = 'us_women';
        }
        else if (sizeType == "EU") {
            sizingType = 'eu_women';
        }
        else if (sizeType == "International"){
            sizingType = 'intl_women';
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

function sizingList(sizing_original, sizeType, gender){ //sizing given from the backend object
    var sizing_list = []
    var category = 'tops'; //once we get subcategory in the db this can be removed and added as arg for the function
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
        case 'us_uk_men_trousers':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<men_trousers.length; j++){
                    if (sizing_original[i].sizing == men_trousers[j].uk || sizing_original[i].sizing == men_trousers[j].us){
                        sizing_list.push(men_trousers[j]);
                    };
                };
            };
            break;
        case 'eu_men_tops':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<men_tops.length; j++){
                    if (sizing_original[i].sizing == men_tops[j].uk){
                        sizing_list.push(men_tops[j]);
                    };
                };
            };
            break;
        case 'eu_men_trousers':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<men_trousers.length; j++){
                    if (sizing_original[i].sizing == men_trousers[j].eu){
                        sizing_list.push(men_trousers[j]);
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
        case 'intl_men_trousers':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<men_trousers.length; j++){
                    if (sizing_original[i].sizing == men_trousers[j].intl){
                        sizing_list.push(men_trousers[j]);
                    };
                };
            };
            break;
        case 'us_women':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<women.length; j++){
                    if (sizing_original[i].sizing == women[j].us){
                        sizing_list.push(women[j]);
                    };
                };
            };
            break;
        case 'uk_women':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<women.length; j++){
                    if (sizing_original[i].sizing == women[j].uk){
                        sizing_list.push(women[j]);
                    };
                };
            };
            break;
        case 'eu_women':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<women.length; j++){
                    if (sizing_original[i].sizing == women[j].eu){
                        sizing_list.push(women[j]);
                    };
                };
            };
            break;
        case 'intl_women':
            for (i=0; i<sizing_original.length; i++){
                for(j=0; j<women.length; j++){
                    if (sizing_original[i].sizing == women[j].intl){
                        sizing_list.push(women[j]);
                    };
                };
            };
            break;
        case 'notype':
            for (i=0; i<sizing_original.length; i++){
                noTypeSizing.uk = sizing_original[i].sizing;
                noTypeSizing.us = sizing_original[i].sizing;
                noTypeSizing.eu = sizing_original[i].sizing;
                noTypeSizing.intl = sizing_original[i].sizing;

                sizing_list.push(noTypeSizing);
            }
    }
    return sizing_list
}