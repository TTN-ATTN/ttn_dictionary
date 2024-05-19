$(document).ready(function () {
    $("#show-history").click(function () {
        $("#history-list").toggle();
    });

    // Attach click event handler to dynamically created history items
    $(document).on("click", ".history-item", function () {
        var clickedWord = $(this).text().trim();
        $("#search-input").val(clickedWord); // Set value of search input field with clicked word
        $("#history-list").hide(); // Hide history list after selection
    });
});
