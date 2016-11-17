$(function () {

var uploaded_csv_data;

$('#submit-k-means').click(function() {
    var k_val = $('#k-value').val();
    reloadKMeansChart(k_val, uploaded_csv_data);
});

 // The event listener for the file upload
    $('#txtFileUpload').change(upload);

    // Method that checks that the browser supports the HTML5 File API
    function browserSupportFileUpload() {
        var isCompatible = false;
        if (window.File && window.FileReader && window.FileList && window.Blob) {
            isCompatible = true;
        }
        return isCompatible;
    }

    // Method that reads and processes the selected file
    function upload(evt) {
        if (!browserSupportFileUpload()) {
          alert('The File APIs are not fully supported in this browser!');
        } else {
            var data = null;
            var file = evt.target.files[0];
            var reader = new FileReader();
            reader.readAsText(file);
            reader.onload = function(event) {
                var csvData = event.target.result;
                data = $.csv.toArrays(csvData);
                if (data && data.length > 0) {
                  uploaded_csv_data = data;
                } else {
                    alert('No data to import!');
                }
            };
            reader.onerror = function() {
                alert('Unable to read ' + file.fileName);
            };
        }
     }


function createKMeansChart(){

    var chart = Highcharts.chart('container', {
            chart: {
                type: 'scatter',
                zoomType: 'xy'
            },
            title: {
                text: 'k-means'
            },
            xAxis: {
                title: {
                    enabled: true,
                    text: 'x'
                },
                startOnTick: true,
                endOnTick: true,
                showLastLabel: true
            },
            yAxis: {
                title: {
                    text: 'y'
                }
            },
            legend: {
                layout: 'vertical',
                align: 'left',
                verticalAlign: 'top',
                x: 100,
                y: 70,
                floating: true,
                backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
                borderWidth: 1
            },
            plotOptions: {
                scatter: {
                    marker: {
                        radius: 2,
                        states: {
                            hover: {
                                enabled: true,
                                lineColor: 'rgb(100,100,100)'
                            }
                        }
                    },
                    states: {
                        hover: {
                            marker: {
                                enabled: false
                            }
                        }
                    },
                    tooltip: {
                        headerFormat: '<b>{series.name}</b><br>',
                        pointFormat: '{point.x} cm, {point.y} kg'
                    }
                }
            }
        });

        return chart;
}

function reloadKMeansChart(k_val, csv_data) {
    $.ajax({
        url: '/k_means_graph_json',
        data: {k: k_val, csv: JSON.stringify(csv_data)},
        type: 'POST',
        success: function(series_data){
            console.log(series_data);
            var chart = createKMeansChart();
            // Add clusters
            $.each(series_data.scatter_plots, function(label, scatter_points) {
                chart.addSeries({
                    name: label,
                    data: scatter_points
                }, false);
            });

            // Add centroids
            chart.addSeries({
                    name: "Centroids",
                    data: series_data.centroids
                }, false);
            chart.redraw();
        }
    });
 }





});