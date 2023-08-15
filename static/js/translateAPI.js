const CLIENT_ID = 'mTtCqhKOF4HIt2NMhBIh'; // 네이버 API 클라이언트 ID
const CLIENT_SECRET = 'd5CfF_r__q'; // 네이버 API 클라이언트 비밀번호

const sourceLang = 'ko'; // 원본 언어
const targetLang = 'en'; // 번역 대상 언어
const textToTranslate = '안녕하세요'; // 번역할 텍스트

fetch('https://openapi.naver.com/v1/papago/n2mt', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    },
    body: `source=${sourceLang}&target=${targetLang}&text=${textToTranslate}`
})
.then(response => response.json())
.then(data => {
    if(data.message && data.message.result) {
        console.log(data.message.result.translatedText);
    } else {
        console.error("Error in translation:", data);
    }
})
.catch(error => {
    console.error('Error:', error);
});
