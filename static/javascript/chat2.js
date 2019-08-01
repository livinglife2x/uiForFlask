
$(".messages").animate({ scrollTop: $(document).height() }, "fast");

function newMessage() {
    message = $(".message-input input").val();
    if ($.trim(message) == '') {
        return false;
    }
    $('<li class="sent"><p>' + message + '</p></li>').appendTo($('.messages ul'));
    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);
    $(".messages").animate({ scrollTop: $(document).height() }, "fast");
    $.ajax({
    url: "/send_message/"+message,
    //data: {'messag':messag,'context':context}
}).done(function(e) {
    newReply(e);
});
};

function newReply(message) {
    if ($.trim(message) == '') {
        return false;
    }
    $('<li class="replies"><p>' + message + '</p></li>').appendTo($('.messages ul'));
    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);
    $(".messages").animate({ scrollTop: $(document).height() }, "fast");
};


$(window).on('keydown', function (e) {
    if (e.which == 13) {
        newMessage();
        newReply();
        return false;
    }
});