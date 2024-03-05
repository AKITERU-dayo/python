// CSVファイルを取得
let csv = new XMLHttpRequest();

// CSVファイルへのパス
csv.open("GET", "date.csv", true); // 非同期に設定

csv.overrideMimeType('text/csv; charset=shift_jis'); // Shift_JISで読み込む

// csvファイル読み込み失敗時のエラー対応
csv.onload = function () {
    if (csv.status === 200) {
        try {
            // 配列を定義
            let csvArray = [];

            // 改行ごとに配列化
            let lines = csv.responseText.split(/\r\n|\n/);

            // 1行ごとに処理
            for (let i = 0; i < lines.length; ++i) {
                let cells = lines[i].split(",");
                if (cells.length != 1) {
                    csvArray.push(cells);
                }
            }
            // コンソールに配列を出力
            console.log(csvArray[0][0]);
            console.log(csvArray.length);

            let csvArraySize = csvArray.length - 1;















            // scenexxxは、各ゲーム画面の要素です
            const sceneTop = document.querySelector('#sceneTop'); // トップ画面の要素
            const sceneGame = document.querySelector('#sceneGame'); // ゲーム画面の要素
            const sceneResult = document.querySelector('#sceneResult'); // リザルト画面の要素

            // 問題文を表示する要素です
            const textQuestion = document.querySelector('#textQuestion'); // 問題文を表示する要素

            // 選択肢を表示する要素です
            const listAnswer = document.querySelector('#listAnswer'); // 選択肢を表示する要素

            // 正解数を表示する要素です
            const numResult = document.querySelector('#numResult'); // 正解数を表示する要素

            // トップ画面にてゲーム開始するボタン要素です
            const btnStart = document.querySelector('#btnStart'); // ゲーム開始ボタンの要素

            const btnAnswer = document.querySelector('#answer');

            const showCorrect = document.querySelector('#correct');
            const showInCorrect = document.querySelector('#in_correct');

            const showNextBtn = document.querySelector('#next');
            


            










            // リザルト画面にて、ゲームをリセットしトップへ戻るボタン要素です
            const btnReset = document.querySelector('#btnReset'); // ゲームリセットボタンの要素

            // ランダムの整数
            /** 重複チェック用配列 */
            let randoms = [];
            /** 最小値と最大値 */
            let min = 0, max = csvArraySize;

            /** 重複チェックしながら乱数作成 */
            for (i = min; i <= max; i++) {
                while (true) {
                    let tmp = intRandom(min, max);
                    if (!randoms.includes(tmp)) {
                        randoms.push(tmp);
                        break;
                    }
                }
            }

            /** min以上max以下の整数値の乱数を返す */
            function intRandom(min, max) {
                return Math.floor(Math.random() * (max - min + 1)) + min;
            }

            // 問題文を格納する要素です
            function shuffle(array) {
                let currentIndex = array.length, temporaryValue, randomIndex;

                // While there remain elements to shuffle...
                while (0 !== currentIndex) {

                    // Pick a remaining element...
                    randomIndex = Math.floor(Math.random() * currentIndex);
                    currentIndex -= 1;

                    // And swap it with the current element.
                    temporaryValue = array[currentIndex];
                    array[currentIndex] = array[randomIndex];
                    array[randomIndex] = temporaryValue;
                }

                return array;
            }

            // let question = [
            //     // 各質問と選択肢、正解を格納する配列
            //     {
            //         text: csvArray[randoms[0]][0],
            //         choice: shuffle([csvArray[randoms[0]][1], csvArray[randoms[1]][1], csvArray[randoms[2]][1], csvArray[randoms[3]][1]]),
            //         answer: csvArray[randoms[0]][1]
            //     },
            //     {
            //         text: csvArray[randoms[1]][0],
            //         choice: shuffle([csvArray[randoms[4]][1], csvArray[randoms[1]][1], csvArray[randoms[5]][1], csvArray[randoms[6]][1]]),
            //         answer: csvArray[randoms[1]][1]
            //     },
            //     {
            //         text: csvArray[randoms[2]][0],
            //         choice: shuffle([csvArray[randoms[7]][1], csvArray[randoms[8]][1], csvArray[randoms[2]][1], csvArray[randoms[9]][1]]),
            //         answer: csvArray[randoms[2]][1]
            //     },
            //     {
            //         text: csvArray[randoms[3]][0],
            //         choice: shuffle([csvArray[randoms[10]][1], csvArray[randoms[11]][1], csvArray[randoms[12]][1], csvArray[randoms[3]][1]]),
            //         answer: csvArray[randoms[3]][1]
            //     }
            // ];

          


            
      
            
            // ラジオボタンのvalue値に応じて問題を追加する
            function addQuestion() {
                let $radioValue = document.querySelector('input:checked[name=radio]').value;
                console.log(`$radioValue: ${$radioValue}`);
                let i = 0;
                question = [
                    
                ]
                for (i = 0; i < $radioValue; i++) {
                    console.log(`$radioValue: ${$radioValue}`);
                    question.push({
                        text: csvArray[randoms[i]][0],
                        choice: shuffle([csvArray[randoms[i]][1], csvArray[randoms[i + 3]][1], csvArray[randoms[i + 4]][1], csvArray[randoms[i + 5]][1]]),
                        answer: csvArray[randoms[i]][1]
                    });
                    console.log(`i: ${showQuestion.length}`);
                }
                i = 1;
            }


            // btnStart.addEventListener("click", questionNum);

            btnStart.addEventListener("click", addQuestion);




















            // ゲームで使用する共通の変数です
            let state = { // ゲームの状態を管理するオブジェクト
                answer: "", // プレイヤーの答えと比較する,正解のテキストです
                gameCount: 0, // プレイヤーが答えた数です
                success: 0, // プレイヤーが答えて、正解した数です
            };

            // ゲームをリセットする関数
            function init() { // ゲームの初期化を行う関数








                state.gameCount = 0; // ゲームカウントをリセット
                state.success = 0; // 正解数をリセット
                changeScene(sceneResult, sceneTop); // リザルト画面からトップ画面へ切り替え

                btnStart.addEventListener("click", gameStart, false); // スタートボタンにクリックイベントを追加
            }

            // 1トップ画面 2.ゲーム画面 3.リザルト画面
            function changeScene(hiddenScene, visibleScene) { // 画面切り替えの関数
                hiddenScene.classList.add("is-hidden"); // 非表示にする画面にis-hiddenクラスを追加
                hiddenScene.classList.remove("is-visible"); // 非表示にする画面からis-visibleクラスを削除
                visibleScene.classList.add("is-visible"); // 表示する画面にis-visibleクラスを追加
            }

            // 問題と選択肢をViewに表示し、正解を共通の変数へ代入
            function showQuestion() { // 問題と選択肢を表示する関数
                let str = "";
                question[state.gameCount].choice.forEach(function (value) {
                    str += '<li class="questionChoice">' + value + "</li>"; // 選択肢をリスト要素としてstrに追加
                });
                textQuestion.innerHTML = question[state.gameCount].text; // 問題文を表示
                listAnswer.innerHTML = str; // 選択肢を表示
            }

            function choiceQuestion() { // 選択肢をクリックしたときの処理を設定する関数
                let questionChoice = document.querySelectorAll(".questionChoice"); // 選択肢の要素を全て取得

                questionChoice.forEach(function (choice) { // 各選択肢に対して
                    choice.addEventListener("click", function () {
                        state.answer = this.textContent; // クリックした選択肢のテキストをstate.answerに代入
                        checkAnswer(question[state.gameCount].answer); // 正解をチェック
                    }, false
                    );
                });
            }

            // 解答が正解か不正解かをチェック
            function checkAnswer(answer) { // 正解をチェックする関数
                if (answer === state.answer) { // 正解の場合
                    correctAnswer();
                } else { // 不正解の場合
                    incorrectAnswer();
                }
                showNextBtn.style.display = "block";
                state.gameCount++; // ゲームカウントを増やす
                if (state.gameCount <= question.length) { // まだ問題が残っている場合

                    // showQuestion(); // 次の問題を表示
                    // choiceQuestion(); // 選択肢のクリックイベントを設定
                } else { // 全ての問題を解き終えた場合


                    gameEnd(); // ゲーム終了
                }
            }

            // 上でチェックし、正解だった場合
            function correctAnswer() { // 正解した場合の処理
                state.success++; // 正解数を増やす
                showCorrect.style.display = "block";   //正解の表示
                // alert("正解"); // 正解のアラートを表示
            }

            // 上でチェックし、不正解だった場合
            function incorrectAnswer() { // 不正解だった場合の処理
                showInCorrect.style.display = "block";
                // alert("不正解"); // 不正解のアラートを表示
            }

            // スタートボタンが押された時
            function gameStart() { // ゲーム開始の関数
                changeScene(sceneTop, sceneGame); // トップ画面からゲーム画面へ切り替え
                showQuestion(); // 最初の問題を表示
                choiceQuestion(); // 選択肢のクリックイベントを設定
            }









            let nextFunc = () => {
                if (state.gameCount === question.length) {
                    showCorrect.style.display = "none";
                    showInCorrect.style.display = "none";
                    showNextBtn.style.display = "none";
                    gameEnd();
                } else {
                    showQuestion();
                    choiceQuestion();
                    showCorrect.style.display = "none";
                    showInCorrect.style.display = "none";
                    showNextBtn.style.display = "none";
                }
            }
            showNextBtn.addEventListener("click", nextFunc);


            // ゲームが終了した時
            function gameEnd() { // ゲーム終了の関数
                showCorrect.style.display = "none";
                showInCorrect.style.display = "none";
                showNextBtn.style.display = "none";
                changeScene(sceneGame, sceneResult); // ゲーム画面からリザルト画面へ切り替え
                numResult.innerHTML = state.success; // 正解数を表示
                btnReset.addEventListener("click", init, false); // リセットボタンにクリックイベントを追加
            }

            // スタートボタンが押されたら、ゲームスタートの関数を
            // リセットボタンが押されたら、ゲーム終了後にゲームリセットする関数を実行するイベント
            init(); // ゲームを初期化
































        } catch (err) {
            console.log(err);
        }
    }
};
csv.send(null);








