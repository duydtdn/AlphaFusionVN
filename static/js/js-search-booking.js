function onSearchDestinationJson() {
            destinationIdSelected = $('#destinationSelected').val();
            startDay = $('#dateCheckIn').val();
            endDay = $('#dateCheckOut').val();
            if(startDay != ''){
                while(startDay.indexOf('/') != -1) {
                startDay = startDay.replace('/', '-');
                }
                while(endDay.indexOf('/') != -1) {
                    endDay = endDay.replace('/', '-');
                }
                location.href = "/search/rq-search-json/"+destinationIdSelected+"/" + startDay + "/" + endDay+ "/";
            }else{
                startDay = '-'
                endDay = '-'
                location.href = "/search/rq-search-json/"+destinationIdSelected+"/" + startDay + "/" + endDay+ "/";
            }

        };