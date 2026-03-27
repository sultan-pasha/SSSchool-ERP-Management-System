// aapl = [
//     { Month: 'يناير', Score: 50 },
//     { Month: 'فبراير', Score: 70 },
//     { Month: 'مارس', Score: 67 },
//     { Month: 'ابريل', Score: 80 },
//     { Month: 'مايو', Score: 95 },
//     { Month: 'يونيو', Score: 70 },
//     { Month: 'يوليو', Score: 97 },
// ];
// const chart = Plot.plot({
//         x: {
//             label: '',
//             domain: [
//                 'يناير',
//                 'فبراير',
//                 'مارس',
//                 'ابريل',
//                 'مايو',
//                 'يونيو',
//                 'يوليو',
//                 'أغسطس',
//                 'سبتمبر',
//                 'أكتوبر',
//                 'نوفمبر',
//                 'ديسمبر',
//             ],
//         },
//         y: { grid: !0, label: '', domain: [0, 100], ticks: 10 },
//         marks: [
//             Plot.ruleY([0]),
//             Plot.areaY(aapl, {
//                 x: 'Month',
//                 y: 'Score',
//                 fillOpacity: 0.7,
//                 fill: '#3a5a97b5',
//                 curve: 'bump-x',
//             }),
//             Plot.lineY(aapl, {
//                 x: 'Month',
//                 y: 'Score',
//                 stroke: '#3a5a97b5',
//                 width: 100,
//                 curve: 'bump-x',
//                 strokeWidth: 5,
//                 basis: 'mean',
//                 marker: 'circle-stroke',
//                 tip: !0,
//             }),
//             Plot.crosshair(aapl, { x: 'Month', y: 'Score' }),
//         ],
//     }),
//     div = document.querySelector('#chart'),
//     area = (div.append(chart), document.querySelector("g[aria-label='area']")),
//     line = document.querySelector("g[aria-label='line']");
// setTimeout(() => {
//     (area.style.opacity = '1'), (area.style.transform = 'scaleX(1) scaleY(1)');
// }, 500),
//     setTimeout(() => {
//         (area.style.opacity = '1'),
//             (line.style.transform = 'scaleX(1) scaleY(1)');
//     }, 800);
