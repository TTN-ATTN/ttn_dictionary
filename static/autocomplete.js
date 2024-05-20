$(document).ready(function() {
    /**
     * Event handler for input event on #search-input element.
     * Fetches autocomplete suggestions based on input prefix.
     */
    $("#search-input").on("input", function() {
        var prefix = $(this).val().trim();
        if (prefix === "") {
            $("#autocomplete-list").empty();
            return;
        }
        $.get("/autocomplete?prefix=" + prefix, function(data) {
            var suggestions = data.suggestions.slice(0, 10);
            var autocompleteList = $("#autocomplete-list");
            autocompleteList.empty();
            suggestions.forEach(function(suggestion) {
                var listItem = $("<li></li>").text(suggestion);
                autocompleteList.append(listItem);
            });
        });
    });

    /**
     * Event handler for click event on dynamically created list items within #autocomplete-list.
     * Populates the search input with the selected suggestion.
     */
    $(document).on("click", "#autocomplete-list li", function() {
        var suggestion = $(this).text();
        $("#search-input").val(suggestion);
        $("#autocomplete-list").empty();
    });
});
