/**
 * require
 *    + jquery
 *    + jquery.pjax
 *    + ShuffleText
 *    + jquery.suffletext
 */

(function() {
  $(document).ready(function() {
    var loading;
    var main;

    loading = $('#loading');
    main = $('#main');

    $('a.js-pjax').pjax('#main', {
      //思ったより spreadsheet からの取得が早くないのと
      //デフォルトのタイムアウトがちょっと見かすぎる気もするので伸ばしておく
      timeout: 5000
    });

    //タイムアウト時の処理
    main.on('pjax:timeout', function() {
      console.log("timeoutttttttttt");
    });

    //pjax(ajax)通信スタート時に呼ばれるイベント
    main.on('pjax:start', function() {
      main.fadeOut(400, function() {
        main.empty();
      });
      loading.fadeIn(500);
    });

    //pjax(ajax)通信完了後に呼ばれるイベント
    main.on('pjax:end', function() {
      var shuffle = $('#show-content').shuffleText();
      loading.fadeOut(400);
      if(shuffle){
          //(　ﾟ∀ﾟ)o彡°Shuffle！Shuffle！
          shuffle.start();
      }
      main.empty().fadeIn(500);
    });
  });
}).call(this);