$(function () {
  $(".chart").easyPieChart({
    size: 195,
    lineWidth: 30,
    barColor: "#e4b425",
    trackColor:"#444",
    scaleColor: false,
    lineCap: "circle",
    animate: ({
        duration: 2000,
        enabled: true
    }),
    rotate: 0,
    onStep: function (from, to, currentValue) {
      this.el.querySelector(".percent").innerText = `${Math.round(
        currentValue
      )}%`;
    },
    onStop:function(cu, x){
      if(x>=90)
      {
        document.querySelector("canvas").style.boxShadow = "0px 0px 20px 10px green"
      }
      if(50<=x && x<90){
        document.querySelector("canvas").style.boxShadow = "0px 0px 20px 10px #67cfff"
      }
      if(0<=x && x<50){
        document.querySelector("canvas").style.boxShadow = "0px 0px 20px 10px red"
      }
    }
  });
});

