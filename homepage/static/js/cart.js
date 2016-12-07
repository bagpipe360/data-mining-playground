$(function () {

$('#submit-cart-data').click(function() {
    reloadCartChart();
});


function createCartChart(cart_data){

    var chart = Highcharts.chart('container', {
        series: [{
            type: 'line',
            name: 'Regression Line 1',
            data: cart_data.line_chart_1,
            marker: {
                enabled: false
            },
            states: {
                hover: {
                    lineWidth: 0
                }
            },
        }, {
            type: 'line',
            name: 'Regression Line 2',
            data: cart_data.line_chart_2,
            marker: {
                enabled: false
            },
            states: {
                hover: {
                    lineWidth: 0
                }
            },
        },
        {
            type: 'scatter',
            name: 'Observations',
            data: cart_data.scatter_plots.data,
            marker: {
                radius: 2.5
            }
        }]
    });

        return chart;
}

function reloadCartChart() {
    var load_sample = false;
    if (typeof csv_data === 'undefined') {
        load_sample = true;
    }
    $.ajax({
        url: '/cart_graph_json',
        data: {load_sample: load_sample},
        type: 'POST',
        success: function(series_data){
            var chart = createCartChart(series_data);

        }
    });
 }





});