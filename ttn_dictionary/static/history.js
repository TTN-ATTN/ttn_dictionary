$(document).ready(function() {
    $('#history-button').click(function() {
        $.get('/history', function(data) {
            $('#history-list').empty();
            for (let word of data['history']) {
                $('#history-list').append('<li><a href="/search?word=' + word + '&mode=vi">' + word + '</a></li>');
            }
            $('#history-list').toggle();
        });
    });
});
