$(document).ready(function () {
    /**
     * Event handler for click event on #show-history element.
     * Toggles the visibility of the #history-list element.
     */
    $("#show-history").click(function () {
        $("#history-list").toggle();
    });

    /**
     * Event handler for click event on dynamically created .history-item elements.
     * Sets the value of #search-input with the clicked word and hides the #history-list.
     */
    $(document).on("click", ".history-item", function () {
        var clickedWord = $(this).text().trim();
        $("#search-input").val(clickedWord);
        $("#history-list").hide();
    });
});
