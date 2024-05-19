$(document).ready(function() {
    $("#search-input").on("input", function() {
        var prefix = $(this).val().trim(); // Trim whitespace from input
        if (prefix === "") {
            $("#autocomplete-list").empty(); // Clear autocomplete list if input is empty
            return; // Exit function if input is empty
        }
        $.get("/autocomplete?prefix=" + prefix, function(data) {
            var suggestions = data.suggestions.slice(0, 10); // Limit suggestions to first 10 elements
            var autocompleteList = $("#autocomplete-list");
            autocompleteList.empty();
            suggestions.forEach(function(suggestion) {
                var listItem = $("<li></li>").text(suggestion);
                autocompleteList.append(listItem);
            });
        });
    });

    // Attach click event handler to dynamically created list items
    $(document).on("click", "#autocomplete-list li", function() {
        var suggestion = $(this).text();
        $("#search-input").val(suggestion);
        $("#autocomplete-list").empty(); // Clear autocomplete list after selection
    });
});
