// 1. 글쓰기와 수정에서 쓸 수 있는 함수
////제목이 비어있거나 또는 5글자 이하라면 경고창 표시하고
////진행 멈춤

////글 내용이 비어있거나 10글자 이하라면 경고창 표시하고 
////진행멈춤
////제목이나 글 내용에 바보, 멍청이, 한조 들어있으면 경고창 표시하고
////진행 멈춤

function validate(title, content){
    let titleValue = document.getElementById("title").value;
    let contentValue = document.getElementById("content").value;

    if(titleValue === "" || titleValue.length < 6){
        alert("제목은 5글자 이상 적어야 되");
        return false;
    }

    if(contentValue === "" || contentValue.length < 11){
        alert("내용은 10글자 이상 적어야 되");
        return false;
    }

    let badWords = ['바보', '멍청이', '한조'];
    for(let i = 0; i < badWords.length; i++){
        if(titleValue.includes(badWords[i]) || contentValue.includes(badWords[i])){
            alert(badWords[i] + "은(는) 사용할 수 없는 단어입니다.");
            return false;
        }
    } 

}

// 2.댓글에서 쓸 수 있는 함수
////댓글 창 비어있으면 경고창 표시
function validateReply(button){
    let buttonText = button.value;

    if (buttonText.includes("쓰기")){
        let text = document.getElementById("replyTextWrite").text;
        
    }
}

