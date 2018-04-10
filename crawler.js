x[0].children[0].children[0].value



var x = document.getElementsByClassName("option-row");
// var newItem = document.createElement("LI");       // Create a <li> node

    // for (var i = 0; i < x.length; i++) {
    //     var newItem = document.createElement("td");
    //     var textnode = document.createTextNode(i);
    //     newItem.appendChild(textnode);
    //     x[i].insertBefore(newItem,x[i].childNodes[0]);
    // }

    var x = document.getElementsByClassName("option-row");

    //claim the arraylist (read xls py)
    brand_list =['Honeywell','HTP','Infinity Drain','Insinkerator','Jet Swet','Julien Sinks','Kohler','Krowne','Lavelle','Legend Valve','Liberty Pumps','Little Giant Pumps','Maid 0 Mist','McDonnell & Miller','Merrill','Mountain Plumbing','Myers Pump','Newport Brass','Noritz','Oasis','Olympia Faucets','Outdoor Shower','Pasco','Peerless Faucets','Robern','Robertshaw','Rohl','Saniflo','Sharkbite','Sioux Chief','Slant/Fin','Sloan Valve','Speakman','Speakman Shower Heads','State Water Heater','SureSeal','Taco','USI','Viega','Watermark','Watts','Zoeller Pumps','Zurn'];

    for (var i = 0; i < x.length; i++) {
        // if element.value in arraylist
        if (brand_list.includes(x[i].children[0].children[0].value)) {
            x[i].childNodes[2].childNodes[0].value = 'exclude'
        }
    }