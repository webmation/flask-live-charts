var chart;
var chart2;

function requestOBS02_Data() {
    $.ajax({
        url: '/obs-0002',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 40; // shift if the series is
                                                 // longer than 40

            // add the point
            chart.series[0].addPoint(point[0], true, shift);
            chart.series[1].addPoint(point[1], true, shift);
            chart.series[2].addPoint(point[2], true, shift);
            chart.series[3].addPoint(point[3], true, shift);
            chart.series[4].addPoint(point[4], true, shift);
            chart.series[5].addPoint(point[5], true, shift);
            chart.series[6].addPoint(point[6], true, shift);
            // chart.series[7].addPoint(point[7], true, shift);

            // call it again after one second
            setTimeout(requestOBS02_Data, 1000);
        },
        cache: false
    });
}

$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'obs-0002-data-container',
            defaultSeriesType: 'spline',
            events: {
                load: requestOBS02_Data
            }
        },
        title: {
            text: '동해신항'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 100,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.001,
            maxPadding: 0.001,
            title: {
                text: 'Value [kPa]',
                margin: 10
            }
        },
        series: [{
            name: 'CH1',
            data: []
        },{
            name: 'CH2',
            data: []
        },{
            name: 'CH3',
            data: []
        },{
            name: 'CH4',
            data: []
        },{
            name: 'CH5',
            data: []
        },{
            name: 'CH6',
            data: []
        },{
            name: 'CH7',
            data: []
        }]
    });
});


function requestOBS03_Data() {
    $.ajax({
        url: '/obs-0003',
        success: function(point) {
            var series = chart2.series[0],
                shift = series.data.length > 40; // shift if the series is
                                                 // longer than 40

            // add the point
            chart2.series[0].addPoint(point[0], true, shift);
            chart2.series[1].addPoint(point[1], true, shift);
            chart2.series[2].addPoint(point[2], true, shift);
            chart2.series[3].addPoint(point[3], true, shift);
            chart2.series[4].addPoint(point[4], true, shift);
            chart2.series[5].addPoint(point[5], true, shift);
            chart2.series[6].addPoint(point[6], true, shift);
            // chart2.series[7].addPoint(point[7], true, shift);

            // call it again after one second
            setTimeout(requestOBS03_Data, 1000);
        },
        cache: false
    });
}

$(document).ready(function() {
    chart2 = new Highcharts.Chart({
        chart: {
            renderTo: 'obs-0003-data-container',
            defaultSeriesType: 'spline',
            events: {
                load: requestOBS03_Data
            }
        },
        title: {
            text: '감천항'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 100,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.001,
            maxPadding: 0.001,
            title: {
                text: 'Value [kPa]',
                margin: 10
            }
        },
        series: [{
            name: 'CH1',
            data: []
        },{
            name: 'CH2',
            data: []
        },{
            name: 'CH3',
            data: []
        },{
            name: 'CH4',
            data: []
        },{
            name: 'CH5',
            data: []
        },{
            name: 'CH6',
            data: []
        },{
            name: 'CH7',
            data: []
        }]
    });
});
