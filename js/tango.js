let inputElement = document.querySelector('input'); // input要素を取得します。

inputElement.oninvalid = function(event) {
    event.target.setCustomValidity('入力必須です');
}

inputElement.oninput = function(event) {
    event.target.setCustomValidity('');
}
