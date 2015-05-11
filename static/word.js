//문서가 준비되면.
$( document ).ready(function() {
    //버튼을 클릭했을 때. button의 id값이 btn-next다.
    $('#btn-next').click(function(){
        nextWord();
    });

    //시작할 때 한번 호출.
    nextWord();
});

function nextWord(){
    $.get( "/word", function( data ) {
        console.log(data);
      $( ".word-body" ).html( data.word );
      $( ".word-meaning" ).html( data.meaning );
    });
}