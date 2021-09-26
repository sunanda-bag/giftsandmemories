if (localStorage.getItem("slide") === null) {
    restore_status();
}
var prod_list = {};
var p_key = 0;
function step2(box_id) {
    if (typeof (Storage) !== "undefined") {
        // Store
        sessionStorage.setItem("box_id", box_id);
        sessionStorage.setItem("slide", 1);
        sessionStorage.setItem("max_val", 1);
    }
    else {
        alert("Sorry, your browser does not support Session Storage...");
    }


    var current = document.getElementById("step1");
    var new_step = document.getElementById("step2");
    current.className = "step0";
    console.log("inside step 2");
    new_step.className = "active step0";
    console.log("inside step 3");

    var cards = document.getElementsByClassName("card1");
    cards[0].className = "card1 b-0";
    cards[1].className = "card1 b-0 show";
}

function step3(prod_id, qty) {

    var p_list = {}

    p_list['product_id'] = prod_id;
    p_list['quantity'] = qty;
    prod_list[p_key] = p_list;
    p_key = p_key + 1;

    if (typeof (Storage) !== "undefined") {
        // Store
        sessionStorage.setItem("product_list", JSON.stringify(prod_list));
        //  console.log(JSON.stringify(prod_list));
        sessionStorage.setItem("slide", 2);
        sessionStorage.setItem("max_val", 2);

    }
    else {
        alert("Sorry, your browser does not support Session Storage...");
    }


    $('#closemodal').click(function () {
        $('#modalwindow').modal('hide');
    });
    $('.modal-backdrop').remove();

    
}

function instep(val, flag) {
    var max_val = parseInt(sessionStorage.getItem("max_val"));
    console.log("type of val: ", typeof (val), val);
    console.log("type of maxval: ", typeof (max_val), max_val);
    if (flag == 1) {
        sessionStorage.setItem("max_val", val);
    }
    
    if (val <= max_val || flag == 1) {
        console.log("before restore status");
        sessionStorage.setItem("slide", val);
        restore_status();
    }

}

function send_data(data_list){
    console.log("inside send data", data_list)
    $.ajax({
        url: '/build_a_box',
        data: {'cart_items':data_list },
        dataType: 'json',
        success: function (res) {
            console.log("successfully sent to view")
        }
    });
}


function restore_status() {

    var mem = sessionStorage.getItem("slide");
    console.log("value of slide1: " + mem);
    if (mem === null) {
        console.log("slide value is null");
    }
    else {
        var data = JSON.parse(JSON.stringify(sessionStorage.product_list));
    
        //var current = document.getElementById("step"+mem);
        var new_step = document.getElementById("step" + (parseInt(mem) + 1));
        //current.className = "step0";
        console.log("inside restore status");



        var cards = document.getElementsByClassName("card1");
        for (var k = 0; k < cards.length; k++) {
            $("#progressbar").children()[k].className = "step0";
            cards[k].className = "card1 b-0";
        }

        new_step.className = "active step0";
        cards[parseInt(mem)].className = "card1 b-0 show";

        var card_count = document.getElementsByClassName("card1").length;
        console.log("befor send data",card_count,(parseInt(mem)+1));  
        if(card_count==(parseInt(mem)+1))
        {
        console.log("calling send data");
        send_data(data);
      }
    }
}


function step4(box_id) {
    sessionStorage.setItem("max_val", 2);
    sessionStorage.setItem("slide", 3);
    var current = document.getElementById("step3");
    var new_step = document.getElementById("step4");
    current.className = "step0";
    console.log("insie step 4");
    new_step.className = "active step0";
    console.log("insie step 5");

    var cards = document.getElementsByClassName("card1");
    cards[2].className = "card1 b-0";
    cards[3].className = "card1 b-0 show";
}




function validate1(val) {
    v1 = document.getElementById("name");
    v2 = document.getElementById("email");

    flag1 = true;
    flag2 = true;

    if (val >= 1 || val == 0) {
        if (v1.value == "") {
            v1.style.borderColor = "red";
            flag1 = false;
        }
        else {
            v1.style.borderColor = "white";
            flag1 = true;
        }
    }

    if (val >= 2 || val == 0) {
        if (v2.value == "") {
            v2.style.borderColor = "red";
            flag2 = false;
        }
        else {
            v2.style.borderColor = "white";
            flag2 = true;
        }
    }

    flag = flag1 && flag2;

    return flag;
}

function validate2(val) {
    v1 = document.getElementById("web-title");
    v2 = document.getElementById("desc");

    flag1 = true;
    flag2 = true;

    if (val >= 1 || val == 0) {
        if (v1.value == "") {
            v1.style.borderColor = "red";
            flag1 = false;
        }
        else {
            v1.style.borderColor = "white";
            flag1 = true;
        }
    }

    if (val >= 2 || val == 0) {
        if (v2.value == "") {
            v2.style.borderColor = "red";
            flag2 = false;
        }
        else {
            v2.style.borderColor = "white";
            flag2 = true;
        }
    }

    flag = flag1 && flag2;

    return flag;
}

$(document).ready(function () {

    var current_fs, next_fs, previous_fs;

    $(".next").click(function () {

        str1 = "next1";
        str2 = "next2";

        if (!str1.localeCompare($(this).attr('id')) && validate1(0) == true) {
            val1 = true;
        }
        else {
            val1 = false;
        }

        if (!str2.localeCompare($(this).attr('id')) && validate2(0) == true) {
            val2 = true;
        }
        else {
            val2 = false;
        }

        if ((!str1.localeCompare($(this).attr('id')) && val1 == true) || (!str2.localeCompare($(this).attr('id')) && val2 == true)) {
            current_fs = $(this).parent().parent().parent();
            next_fs = $(this).parent().parent().parent().next();

            $(current_fs).removeClass("show");
            $(next_fs).addClass("show");

            $("#progressbar li").eq($(".card").index(next_fs)).addClass("active");

            current_fs.animate({}, {
                step: function () {

                    current_fs.css({
                        'display': 'none',
                        'position': 'relative'
                    });

                    next_fs.css({
                        'display': 'block'
                    });
                }
            });
        }
    });

    $(".prev").click(function () {

        current_fs = $(this).parent();
        previous_fs = $(this).parent().prev();

        $(current_fs).removeClass("show");
        $(previous_fs).addClass("show");

        $("#progressbar li").eq($(".card").index(next_fs)).removeClass("active");

        current_fs.animate({}, {
            step: function () {

                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });

                previous_fs.css({
                    'display': 'block'
                });
            }
        });
    });

});