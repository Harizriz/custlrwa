var men_tops = [
    {
        "uk": "34",
        "us": "34",
        "eu": "44",
        "intl": "xs"
    },
    {
        "uk": "36",
        "us": "36",
        "eu": "46",
        "intl": "s"
    },
    {
        "uk": "38",
        "us": "38",
        "eu": "48",
        "intl": "m"
    },
    {
        "uk": "40",
        "us": "40",
        "eu": "50",
        "intl": "l"
    },
    {
        "uk": "42",
        "us": "42",
        "eu": "52",
        "intl": "xl"
    },
    {
        "uk": "44",
        "us": "44",
        "eu": "54",
        "intl": "xxl"
    },
    {
        "uk": "46",
        "us": "46",
        "eu": "56",
        "intl": "xxxl"
    }
];

var men_trousers = [
    {
        "uk": "28",
        "us": "28",
        "eu": "44",
        "intl": "xs"
    },
    {
        "uk": "32",
        "us": "32",
        "eu": "46",
        "intl": "s"
    },
    {
        "uk": "34",
        "us": "34",
        "eu": "48",
        "intl": "m"
    },
    {
        "uk": "36",
        "us": "36",
        "eu": "50",
        "intl": "l"
    },
    {
        "uk": "38",
        "us": "38",
        "eu": "52",
        "intl": "xl"
    },
    {
        "uk": "40",
        "us": "40",
        "eu": "54",
        "intl": "xxl"
    },
    {
        "uk": "42",
        "us": "42",
        "eu": "56",
        "intl": "xxxl"
    }
];

var women = [
    {
        "uk": "2",
        "us": "00",
        "eu": "30",
        "intl": "xs"
    },
    {
        "uk": "4",
        "us": "0",
        "eu": "32",
        "intl": "xs"
    },
    {
        "uk": "6",
        "us": "2",
        "eu": "34",
        "intl": "s"
    },
    {
        "uk": "8",
        "us": "4",
        "eu": "36",
        "intl": "s"
    },
    {
        "uk": "10",
        "us": "6",
        "eu": "38",
        "intl": "m"
    },
    {
        "uk": "12",
        "us": "8",
        "eu": "40",
        "intl": "m"
    },
    {
        "uk": "14",
        "us": "10",
        "eu": "42",
        "intl": "l"
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
    if (gender == 'men'){
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
    else{ //women's tops and trousers are the same
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
    return sizingType;
}

function sizingList(sizing, gender){ //sizing given from the backend object
    var sizing_list = []
    var category = 'tops'; //once we get subcategory in the db this can be removed and added as arg for the function
    var sizingType = sizingDetection(sizeType, gender, category)
    var i=0;
    switch(sizingType){
        case 'us_uk_men_tops':
            //for loop to look through the original sizing list, match with sizes on the input sizing for this function, then += to sizing_list
            for (i=0; i < men_tops.length; i++){
                if (men_tops[i].uk == sizing[i].sizing || men_tops[i].us == sizing[i].sizing){
                    sizing_list += men_tops[i];
                }
            };
            break;
        case 'us_uk_men_trousers':
            for (i=0; i < men_trousers.length; i++){
                if (men_trousers[i].uk == sizing[i].sizing || men_trousers[i].us == sizing[i].sizing){
                    sizing_list += men_trousers[i];
                }
            };
            break;
        case 'eu_men_tops':
            for (i=0; i < men_tops.length; i++){
                if (men_tops[i].eu == sizing[i].sizing){
                    sizing_list += men_tops[i];
                }
            };
            break;
        case 'eu_men_trousers':
            for (i=0; i < men_trousers.length; i++){
                if (men_trousers[i].eu == sizing[i].sizing){
                    sizing_list += men_trousers[i];
                }
            };
            break;
        case 'intl_men_tops':
            for (i=0; i < men_tops.length; i++){
                if (men_tops[i].intl == sizing[i].sizing){
                    sizing_list += men_tops[i];
                }
            };
            break;
        case 'intl_men_trousers':
            for (i=0; i < men_trousers.length; i++){
                if (men_trousers[i].intl == sizing[i].sizing){
                    sizing_list += men_trousers[i];
                }
            };
            break;
        case 'us_women':
            for (i=0; i < women.length; i++){
                if (women[i].us == sizing[i].sizing){
                    sizing_list += women[i];
                }
            };
            break;
        case 'uk_women':
            for (i=0; i < women.length; i++){
                if (women[i].uk == sizing[i].sizing){
                    sizing_list += women[i];
                }
            };
            break;
        case 'eu_women':
            for (i=0; i < women.length; i++){
                if (women[i].eu == sizing[i].sizing){
                    sizing_list += women[i];
                }
            };
            break;
        case 'intl_women':
            for (i=0; i < women.length; i++){
                if (women[i].intl == sizing[i].sizing){
                    sizing_list += women[i];
                }
            };
            break;
        case 'notype':
            for (i=0; i<sizing.length; i++){
                noTypeSizing.uk = sizing[i].sizing;
                noTypeSizing.us = sizing[i].sizing;
                noTypeSizing.eu = sizing[i].sizing;
                noTypeSizing.intl = sizing[i].sizing;

                sizing_list += noTypeSizing;
            }
    }
    return sizing_list
}