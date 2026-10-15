/**
 * 远程接口调用代理类
 */
//var SERVICE_ADDRESS = "http://106.52.123.137";
var SERVICE_ADDRESS = "http://localhost:9527";

/**
 * 处理rest请求结果
 * 
 * @param {Http请求} xhr 
 * @param {回调处理函数} handlerFun 
 * @returns 函数对象
 */
function handleResult(xhr, handlerFun){
    return function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            // 未授权或者token过期，跳转到登录页面
            if (xhr.status == 401) {
                window.location.href = "./login.html";
            }
        }

        var result = JSON.parse(xhr.responseText);
        handlerFun(result);
    }
}

/**
 * 默认回调方法. 此方法不对接口返回结果做任何处理, 用于绑定处理401的情况
 * 
 * @param {接口返回结果} result 
 */
function defaultHandleFun(result){

}

/**
 * 发送验证码到用户的账号邮箱
 *  
 * @param {邮箱账号} account 
 */
function sendVerifyCodeProxy(account){
    var xhr = new XMLHttpRequest();
    var requestPath = SERVICE_ADDRESS + "/neo-lesson-mgmt/v1/login/generate-verify-code";

    xhr.open("POST", requestPath, true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.send(account);
}

/**
 * 登录接口代理
 * 
 * @param {用户登录数据} userLogin 
 * @param {回调处理函数} handlerFun 
 */
function loginProxy(userLogin, handlerFun){
    var xhr = new XMLHttpRequest();
    var requestPath = SERVICE_ADDRESS + "/neo-lesson-mgmt/v1/login/login-in";
    xhr.onload = handleResult(xhr, handlerFun);

    xhr.open("POST", requestPath, false);
    xhr.setRequestHeader('Content-Type', 'application/json');

    const userLoginJson = JSON.stringify(userLogin);
    xhr.send(userLoginJson);
}
