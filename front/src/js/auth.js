
// 点击登录按钮，弹出模态对话框
// 点击右上角能关闭对话框
$(function () {
    $("#btn").click(function () {
        $(".mask-wrapper").show();
    });

    $(".close-btn").click(function () {
        $(".mask-wrapper").hide();
    });
});


$(function () {
    $(".switch").click(function () {
        var scrollWrapper = $(".scroll-wrapper");
        var currentLeft = scrollWrapper.css("left");
        currentLeft = parseInt(currentLeft);
        if(currentLeft < 0){
            // 添加平移动画
            scrollWrapper.animate({"left":'0'});
        }else{
            scrollWrapper.animate({"left":"-10.6667rem"});
        }
    });
});