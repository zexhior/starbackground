function getRandomNumber(min, max){
    return Math.random() * (max - min) + min;
}

for (var i = 0; i < 500; i++){
    var etoile = document.createElement('div');
    var w = Math.floor(getRandomNumber(3, 6));
    var pos_x = Math.floor(getRandomNumber(0, 1800));
    var pos_y = Math.floor(getRandomNumber(0, 600));
    var border = w / 10;
    $(etoile).css({
        background: 'white',
        position: 'absolute',
        width: w+'px',
        height: w+'px',
        'border-radius': '50%',
        border : border+'px '+border+'px '+border+'px '+border+'px solid gray',
        transform : 'translate('+pos_x+'px,'+pos_y+'px)'
    });
    $('body').append(etoile);   
}

$('body').css({
    background : 'rgb(0, 0, 29)'
});