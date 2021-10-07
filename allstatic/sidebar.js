$(document).ready(function () {
    var bar = $(".side")
    var dashboard = $(".dashboard")
    if (bar.css("display") === "block") {
        // bar.css({display: "none"})
        dashboard.addClass("sidebar-active")
    }

    var sideBar = (function() {
        var dashboardclass = dashboard.attr("class")

        if (dashboardclass.includes("sidebar-active")) {
            bar.css(
                {
                    // display: "none",
                    transform: "translateX(-300px)",
                    opacity: 0
                }
            )
            dashboard.removeClass("sidebar-active")
        } else {
            bar.css(
                {
                    // display: "block",
                    transform: "translateX(0px)",
                    opacity: 1
                }
            )
            dashboard.addClass("sidebar-active")
        }
    })

    $(".trigger-for-sidebar").on("click", function(e) {
        sideBar()
    })
});