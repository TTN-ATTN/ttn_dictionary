$(document).ready(function() {
    $("#search-input").on("input", function() {
        var prefix = $(this).val();
        $.get("/autocomplete?prefix=" + prefix, function(data) {
            var suggestions = data.suggestions;
            var autocompleteList = $("#autocomplete-list");
            autocompleteList.empty();
            suggestions.forEach(function(suggestion) {
                var listItem = $("<li></li>");
                var link = $("<a></a>").text(suggestion);
                listItem.append(link);
                autocompleteList.append(listItem);
            });
        });
    });

    // Attach click event handler to dynamically created list items
    $(document).on("click", "#autocomplete-list li", function() {
        var suggestion = $(this).text();
        $("#search-input").val(suggestion);
    });
});
