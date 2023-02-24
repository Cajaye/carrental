let autocomplete;
function initAutoComplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('autocomplete'),
        {
            types:['establishment'],
            componentRestrictions:{'country':'jm'},
            fields:['place_id','geometry','name']
        }
    )

    autocomplete.addListener('place_changed', onPlaceChanged)
}

function onPlaceChanged() {
    let place = autocomplete.getPlace()

    if (!place.geometry){ //if place entered does not exist reset form field
        document.getElementById('autocomplete').placeholder = 'Enter a place...'
    }else{
        document.getElementById('autocomplete').value = place.name
    }
}