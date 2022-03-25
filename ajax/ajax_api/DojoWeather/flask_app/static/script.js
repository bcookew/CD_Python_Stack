function alertCity(element){
    alert(`Weather data for ${element.innerText} not available!`)
}

function remEl(elID) {
    document.getElementById(elID).remove()    
}

var tempInit = "C";
let tempFormat = "metric"
function tempConvert(element){
    if(element.value === tempInit){
        return;
    } 
    var temps = document.querySelectorAll(".temp");
    if(element.value === "C"){
        tempInit = "C"
        tempFormat = "Celsius"
        for(el of temps){
            el.innerText = Math.round((el.innerText - 32)*5/9);
        }
    }
    if(element.value === "F"){
        tempInit = "F"
        tempFormat = "imperial"
        for(el of temps){
            el.innerText = Math.round(el.innerText/5*9+32);
        }
    }
}

async function get_location(zipcode) {
    var response = await fetch(`http://api.openweathermap.org/geo/1.0/zip?zip=${zipcode},US&appid=7119f6ee6d8eb24b6f371c9782b1ef5e`);
    var location_data = await response.json();
    console.log(location_data);
    return get_weather(location_data);
}
async function get_weather(location_data) {
    var response = await fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${location_data['lat']}&lon=${location_data['lon']}&exclude=minutely,hourly,alerts&appid=7119f6ee6d8eb24b6f371c9782b1ef5e&units=${tempFormat}`);
    var weather_data = await response.json();
    console.log(weather_data);
    return weather_data;
}

$(function(){
    $(".city-link").click(async function(){
        let weather_data = await get_location(this.value);
        let city_name = $(this).text()
        $("#city_name").text(city_name)
        $("#day0 .highTemp .temp").text(weather_data['daily'][0]['temp']['max'])
        $("#day0 .lowTemp .temp").text(weather_data['daily'][0]['temp']['min'])
        $("#day0 .description").text(weather_data['daily'][0]['weather'][0]['main'])
        $("#day1 .highTemp .temp").text(weather_data['daily'][1]['temp']['max'])
        $("#day1 .lowTemp .temp").text(weather_data['daily'][1]['temp']['min'])
        $("#day1 .description").text(weather_data['daily'][1]['weather'][0]['main'])
        $("#day2 .highTemp .temp").text(weather_data['daily'][2]['temp']['max'])
        $("#day2 .lowTemp .temp").text(weather_data['daily'][2]['temp']['min'])
        $("#day2 .description").text(weather_data['daily'][2]['weather'][0]['main'])
        $("#day3 .highTemp .temp").text(weather_data['daily'][3]['temp']['max'])
        $("#day3 .lowTemp .temp").text(weather_data['daily'][3]['temp']['min'])
        $("#day3 .description").text(weather_data['daily'][3]['weather'][0]['main'])
    });
});