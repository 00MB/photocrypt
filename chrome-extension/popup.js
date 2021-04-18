document.addEventListener('DOMContentLoaded', function() {
    var submitLinkButton = document.getElementById('submitLink');
    submitLinkButton.addEventListener('click', function() {
        // chrome.runtime.sendMessage({msg: 'file_input'});
        console.log("Here!");
    });
    // checkPageButton.addEventListener('click', function() {
    //     chrome.tabs.getSelected(null, function(tab) {
    //         d = document;

    //         var f = d.createElement('form');
    //         f.action = 'http://gtmetrix.com/analyze.html?bm';
    //         f.method = 'post';
    //         var i = d.createElement('input');
    //         i.name = 'url';
    //         i.value = tab.url;
    //         f.appendChild(i);
    //         d.body.appendChild(f);
    //         f.submit();
    //     });
    // }, false);
}, false);