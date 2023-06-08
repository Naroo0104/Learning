function goMessage(mode){
    alert("호출됐습니다.");
    document.getElementById(mode).innerHTML="임의의 값 넣기" + mode;
}