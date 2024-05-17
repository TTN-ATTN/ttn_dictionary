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
                var mode = $("#mode-select").val();
                link.attr("href", "/search?word=" + encodeURIComponent(suggestion) + "&mode=" + mode); 
                listItem.append(link);
                autocompleteList.append(listItem);
            });
        });
    });
});
