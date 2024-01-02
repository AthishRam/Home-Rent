function onPageLoad() {

    var locationUrl = "http://127.0.0.1:5000/get_location_names";
    $.get(locationUrl, function(data) {
        if (data) {
            var locations = data.locations;
            var uiLocations = $("#uiLocations");
            uiLocations.empty();
            uiLocations.append($('<option>', {
                value: '', text: 'Location', disabled:"disabled", selected:"selected"
            }));
            for (var i in locations) {
                var opt = new Option(locations[i]);
                uiLocations.append(opt);
            }
        }
    });

    var furnishingUrl = "http://127.0.0.1:5000/get_furnishing_type";
    $.get(furnishingUrl, function(data) {
        if (data) {
            var furnishing = data.furnishing;
            var uiFurnishing = $("#uiFurnishing");
            uiFurnishing.empty();
            uiFurnishing.append($('<option>', {
                value: '',text: 'Furnishing Type',disabled:"disabled", selected:"selected"
      }));
            for (var i in furnishing) {
                var opt = new Option(furnishing[i]);
                uiFurnishing.append(opt);
            }
        }
    });

    var bhk = [1, 2, 3, 4];
    var bhkSelect = document.getElementById("bhk");
    for (var i = 0; i < bhk.length; i++) {
        var option = document.createElement("option");
        option.value = bhk[i];
        option.text = bhk[i] + "\tBedroom";
        bhkSelect.add(option);
    }
}

function onClickedEstimatePrice(){
    var form = document.querySelector(".form");
    var formData = new FormData(form);
    var bhk = formData.get("bhk");
    var location = formData.get("uiLocations");
    var size = formData.get("size");
    var furnishing = formData.get("uiFurnishing");

    var url = "http://127.0.0.1:5000/predict_home_price";
    $.post(url, {
        size: size,
        bhk: bhk,
        furnishing: furnishing,
        location: location
    }, function(data, status) {
        var price = data.estimated_price.toString()
        $("#result").html("Estimated rent for an\t"+furnishing.toLowerCase()+"\t"+bhk+"\tbedroom apartment with\t"+size+"\tsquare feet in\t"+location+"\tis\t"+price+"\tRupees");
    });
  }
window.onload = onPageLoad;