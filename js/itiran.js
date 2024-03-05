
// const titleTest = document.querySelector('h1'); // ゲーム開始ボタンの要素

// titleTest.addEventListener("click", testFunc, false); // スタートボタンにクリックイベントを追加


// function testFunc() {
//     alert('hi');
// }


// const edit = document.querySelectorAll('div');  //div要素を取得

// edit.forEach(e => console.log(e.style));


// let changecolor = () => {
//     mean.classList.toggle("white");
// }



const $hiddenBtn = document.querySelector('.hiddenbtn');
const $mean = document.querySelectorAll("dd");

let color_change = 0;
let hover_color = 0;
let $background = document.querySelector('body');


// 各dd要素に対してイベントリスナーを設定
// let hoverChange = () => {
//     // マウスが要素の上に乗ったときのイベント
//     element.addEventListener('mouseover', () => {
//         element.style.color = 'black';
//         element.style.background = 'white';
//     });

//     // マウスが要素から離れたときのイベント
//     element.addEventListener('mouseout', () => {
//         element.style.color = 'red';
//         element.style.background = 'red';
//     });
// }

console.log(color_change);
$hiddenBtn.addEventListener("click", () => {
    if (color_change == 0) {
        document.querySelectorAll('dd').forEach(function (element) {
            element.style.color = "#3CB371";
            element.style.background = "#3CB371";

            $hiddenBtn.textContent = "表示";

            element.style.transition='all 0.3s ease';
            element.addEventListener('mouseover', () => {
                element.style.color = 'black';
                element.style.background = 'white';
            });

            // マウスが要素から離れたときのイベント
            element.addEventListener('mouseout', () => {
                element.style.color = '#3CB371';
                element.style.background = '#3CB371';
            });
        });
        color_change = 1;
    } else {
        document.querySelectorAll('dd').forEach(function (element) {
            element.style.color = "black";
            element.style.background = "white";
            $hiddenBtn.textContent = "非表示";

            element.addEventListener('mouseover', () => {
                element.style.color = 'black';
                element.style.background = 'white';
            });


            element.addEventListener('mouseout', () => {
                element.style.color = 'black';
                element.style.background = 'white';
            });




        });
        color_change = 0;
    }
})

// document.querySelectorAll('dd').addEventListener("mouseover", () => {
//     this.forEach(function (e){
//         alert('hoeverしたよ');

//         this.style.color = none;
//     })
// })

// document.querySelector('dd').addEventListener("mouseout", () => {
    //     // alert('hoeverはずしたよ');
    //     this.style.color = "red";
    // })

// セレクタ名（.pagetop）に一致する要素を取得
const pagetop_btn = document.querySelector(".pagetop");

// .pagetopをクリックしたら
pagetop_btn.addEventListener("click", scroll_top);

// ページ上部へスムーズに移動
function scroll_top() {
  window.scroll({ top: 0, behavior: "smooth" });
}

// スクロールされたら表示
window.addEventListener("scroll", scroll_event);
function scroll_event() {
  if (window.pageYOffset > 100) {
    pagetop_btn.style.opacity = "1";
  } else if (window.pageYOffset < 100) {
    pagetop_btn.style.opacity = "0";
  }
}


    
    
    document.querySelector('.pagetop').addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    




//====================================================//
let elements = document.querySelectorAll('.test_element');
//====================================================//

for (let i = 0; i < elements.length; i++) {
    elements[i].style.color = "white";
    $hiddenBtn.textContent = "表示";
}

//これを省略して書いたのが↓
elements.forEach(function (element) {
    element.style.color = "black";
    $hiddenBtn.textContent = "非表示";
})

let j = 0;
while (j < element.length) {
    elements[j].style.color = "white";
    $hiddenBtn.textContent = "表示";
    ++j;
}










