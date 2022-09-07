$(function() {
    // 註冊 方案一 的 "大項" 點擊事件
    $('#titleA').click(function(event) {
        let is_checked = $(this).prop('checked');
        if (is_checked) {
            $('#detailA').slideDown();
        } else {
            $('#detailA').slideUp();
        }
    })

    // 註冊 方案二 的 "大項" 點擊事件
    $('#titleB').click(function(event) {
        let is_checked = $(this).prop('checked');
        if (is_checked) {
            $('#detailB1').prop('checked', true);
            $('#detailB2').prop('checked', true);
        } else {
            $('#detailB1').prop('checked', false);
            $('#detailB2').prop('checked', false);
        }
    })

    // 註冊 方案三 的 "大項" 點擊事件
    $('#titleC').click(function(event) {
        let is_checked = $(this).prop('checked');
        if (is_checked) {
            $('#detailC').slideDown();
            $('#all').show();
            $('#inv').show();
        } else {
            $('#detailC').slideUp();
            $('#all').hide();
            $('#inv').hide();
        }
    })

    // 註冊 方案三 的 "全選" 點擊事件
    $('#all').click(function(event) {
        $('#detailC1').prop('checked', true);
        $('#detailC2').prop('checked', true);
    })

    // 註冊 方案三 的 "取消" 點擊事件
    $('#inv').click(function(event) {
        $('#detailC1').prop('checked', false);
        $('#detailC2').prop('checked', false);
    })

})