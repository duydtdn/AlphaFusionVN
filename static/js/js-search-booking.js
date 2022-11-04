function onSearchDestinationJson() {
    destinationIdSelected = $('#destinationSelected').val();
    startDay = $("input[name=t-start]").val();
    endDay = $("input[name=t-end]").val();
    // alert(document.querySelector('input[name=t-end]').value);
    // alert($("input[name=t-end]").val());
    if (startDay != '') {
        while (startDay.indexOf('/') != -1) {
            startDay = startDay.replace('/', '-');
        }
        while (endDay.indexOf('/') != -1) {
            endDay = endDay.replace('/', '-');
        }
        location.href = "search/rq-search-json/" + destinationIdSelected + "/" + startDay + "/" + endDay + "/";
    } else {
        startDay = '-'
        endDay = '-'
        location.href = "search/rq-search-json/" + destinationIdSelected + "/" + startDay + "/" + endDay + "/";
    }

};