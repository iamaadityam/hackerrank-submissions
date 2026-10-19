(function () {
          var p = window.location.pathname;
          // Routes whose React shell renders in light skip the pre-paint dark
          // flip to avoid a dark→light flicker. Keep in sync with
          // isDarkThemeEnabledOnRoute in src/shared/community/util/common.ts.
          var LIGHT_ONLY = [/^\/settings\/personalization(\/|$)/];
          var forcedLight = LIGHT_ONLY.some(function (re) { return re.test(p); });
          if (!forcedLight && document.cookie.indexOf('user_theme=dark') > -1) {
            document.body.setAttribute('data-theme', 'dark');
          }
        })();
      
    
  


  
    

  
  
  
  

  |PrepareCertifyCompete|Switch to..All ContestsCSE IP101 Lab - Week-7 (Monday)Password Generator 8Password Generator 8ProblemSubmissionsLeaderboardDiscussions.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
Passwords are built from this 36-character alphabet (the letters a to z, then the digits 0 to 9):

abcdefghijklmnopqrstuvwxyz0123456789

Positions start at 0: 'a' is 0, 'b' is 1, ... 'z' is 25, '0' is 26, ... '9' is 35.

What is a seed? It is a starting number for Python's random number generator. The same seed always gives the same "random" numbers. random.seed(s) sets the seed, and random.randint(0, 35) returns a random whole number from 0 to 35 (both included).

Given a seed s and a length n, print the password of length n.

To get the same result as everyone else: set the seed once with random.seed(s), then create the characters from left to right, calling random.randint(0, 35) once for each character. Each number is that character's position in the alphabet.

Example: s = 1, n = 3. The three calls to random.randint(0, 35) give 8, 4, 16. Positions 8, 4, 16 are 'i', 'e', 'q', so the password is ieq.

Use only random.seed() and random.randint().Input Format.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
Two values, each on its own line:
  1. s, the seed (an integer)
  2. n, the length of the password (an integer)Constraints.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
0 <= s <= 1,000,000
1 <= n <= 50Output Format.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
A single line containing the password of length n.Sample Input 0.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
1
8

Sample Output 0.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
ieqh524y

Change ThemeLanguage: Python 3More# Enter your code here. Read input from STDIN. Print output to STDOUTLine: 1 Col: 70Submit CodeRun CodeUpload Code as FileTest against custom inputAuthorabhishek26008DifficultyHardMax Score6Submitted By148Need Help?View discussionsView top submissionsrate this challengeMORE DETAILSDownload problem statementDownload all test casesSuggest EditsShare on XShare on LinkedInBlogScoringEnvironmentFAQAbout UsHelpdeskCareersTerms Of ServicePrivacy Policy

  
  HR = window.HR || {};
  HR.development = false;
  HR.assetPath = 'https://hrcdn.net/fcore/assets/';
  HR.pageLoadTime = Date.now();
  HR.serverAPITime = 446
  HR.serverRenderTime = 7

  HR.production = true;
  HR.devServer = false;
  HR.isIsomorphic = true;
  HR.loadedWithOldCss = false;
  HR.pusher = {"key":"a280047e3b323ccb1b65","cluster":"mt1"};




  



  
  
    
      Cookie support is required to access HackerRank
    
    Seems like cookies are disabled on this browser, please enable them to open this website
  

  
    (function() {
      document.getElementById("cookies-check").style.display = navigator.cookieEnabled ? "none": "block";
    })()
  
  

  
    // HR namespace
    HR = window.HR || {};
    HR.firebaseConfig = {"apiKey":"AIzaSyChKw1eFkv7iEgkqCDlt3Smbe0GMTn_CkY","authDomain":"codepair.firebaseapp.com","databaseURL":"https://codepair.firebaseio.com","projectId":"project-1659471146556770367","storageBucket":"project-1659471146556770367.appspot.com","messagingSenderId":"455600305505","appId":"1:455600305505:web:a61d86862cadda4e378120"};
    HR.productNamespace = 'hackerrank';
    HR.stripe = {"key":"pk_PBXVCPHjyi31lIcbSe2mnlWEIYUzG"};
    HR.microsoftConfigClientId = "";
    HR.microsoftConfigTenantId = "";
    HR.servicesBaseUrl = "https://services.hackerrank.com";
    HR.integrationsBackendBaseUrl = "";
    HR.pendoAPIKey = "6a49047d-7d4c-46f5-7b81-8b6193d6bf7b";
    HR.googleAuthClientId = "539603982008.apps.googleusercontent.com";
    HR.quickApplyId = "mmlghgaenodejbokcogohcjelnogcckl";
    HR.openReplayCloudProjectKey = "Fh8O2RD6uG7D5xFUzCND";
    HR.openReplayProjectKey = "";
    HR.openReplayIngestionUrl = "";
    HR.lspBaseUrl = "hrc.suggest.hackerrank.com";
    HR.krakendHost = "appgateway.hackerrank.com";
    HR.analyticsHost = "https://www.hackerrank.com/appgateway";
    HR.llmGatewayUrl = "https://platform.ai.hackerrank.com";

    // Set window properties
    window.LOG_LEVEL = 'error';
    window.APPLICATION_ENV = '';
    window.NEW_RELIC_APP_NAME = 'community-frontend-production';

    window.__HR__ = {};
  

  

  var getUser = (function () {
    var userData;
    if (HR.userEmitter && typeof HR.userEmitter.on === 'function') {
      HR.userEmitter.on('initializeNewUser', function(user) {
        userData = user;
      });
    }
    try {
      if (typeof userData === 'undefined') {
        var initialDataElm = document.querySelector('#initialUserData');
        userData = JSON.parse(decodeURI(initialDataElm.innerHTML));
        initialDataElm.remove();
      }
    } catch (e) {
      userData = {};
      console.log('No initial User data found');
    }
    return function () {
      return userData;
    };
  })();




  var _gaq = _gaq || [];
  
















var gtmTracking = function (user){
  if (window.dataLayer) {
    

      
        window.dataLayer.push({
          'event': 'identify',
          onboardingStatus: user.onboarding_status,
          signupIntent: user.signup_intent,
          isProfessional: user.is_professional,
        });
      
    }
}
gtmTracking(getUser());
if (HR.userEmitter && typeof HR.userEmitter.on === 'function') {
  HR.userEmitter.on('initializeNewUser', function(user) {
    gtmTracking(user);
  });
}









  window.plausible =
    window.plausible ||
    function () {
      (window.plausible.q = window.plausible.q || []).push(arguments);
    };






<iframe
    src="https://www.googletagmanager.com/ns.html?id=GTM-PX2ZJF2"
    height="0"
    width="0"
    style="display: none; visibility: hidden"
  ></iframe
>









  
  (function() {
    if(typeof hr_metrics !== 'undefined' && hr_metrics.init ) {
        hr_metrics.init({
          product: 'hackerrank',
          use_cookie: true,
          uid_cookie_key: 'hackerrank_mixpanel_token',
          uid_token_cookie_key: 'metrics_user_identifier',
          session_cookie_key: 'session_id',
          metrics_endpoint:  'https://metrics.hackerrank.com/metrics' 
        });
    }
  })();
  
  (function(h) {
    window.hr_metrics = h;
    if (!h.loaded) {
      var a = ['track', 'batch_track', 'app_track', 'externalService', 'init', 'batch_track_record', 'track_dwell_time', 'set_navigation_data'];
      for (var i = 0; i < a.length; i++) {
        if (!h[a[i]]) {h[a[i]] = function() {};}
      }
    }
  })(window.hr_metrics || {});


  





  
  
    if (('performance' in window) && ('timing' in window.performance)) {
      window.addEventListener('load', function() {
        setTimeout(function(){
          var timing = window.performance.timing;
          var obj = {
            referring_url: window.location.pathname,
            fullLoadTime: timing.loadEventEnd - timing.navigationStart,
            // Total time from req start to load
            loadTime: timing.loadEventEnd - timing.fetchStart,
            // Time spent constructing the DOM tree
            domReadyTime: timing.domComplete - timing.domInteractive,
            // Time consumed preparing the new page
            readyStart: timing.fetchStart - timing.navigationStart,
            // Time spent during redirection
            redirectTime: timing.redirectEnd - timing.redirectStart,
            // AppCache
            appcacheTime: timing.domainLookupStart - timing.fetchStart,
            // Time spent unloading documents
            unloadEventTime: timing.unloadEventEnd - timing.unloadEventStart,
            // DNS query time
            lookupDomainTime: timing.domainLookupEnd - timing.domainLookupStart,
            // TCP connection time
            connectTime: timing.connectEnd - timing.connectStart,
            // Time spent during the request
            requestTime: timing.responseEnd - timing.requestStart,
            // Time to first byte for the request
            timeToFirstByte: timing.responseStart - timing.requestStart,
            // Request to completion of the DOM loading
            initDomTreeTime: timing.domInteractive - timing.responseEnd,
            // Load event time
            loadEventTime: timing.loadEventEnd - timing.loadEventStart,
            // Origin of the request
            react: true,
            //isIsomorphic flag
            isIsomorphic: window.HR.isIsomorphic,
            //old css loaded flag
            loadedWithOldCss: window.HR.loadedWithOldCss,
            // server timings
            serverAPITime: window.HR.serverAPITime,
            serverRenderTime: window.HR.serverRenderTime,
          }

          if (('navigation' in window.performance) && ('getEntries' in window.performance)) {
            obj.navigationType = window.performance.navigation.type;
            obj.navigationRedirectCount = window.performance.navigation.redirectCount;
            if (obj.fullLoadTime > 8000) {
              try {
                var entries = window.performance.getEntries();
                if(entries[0].toJSON){
                  obj.networkRequests = entries.map(function(e) {return e.toJSON();});
                }
              } catch (e) {
                //do nothing
              }
            }
          }
          if(hr_metrics && hr_metrics.app_track) hr_metrics.app_track('page-load-metrics', obj);
        }, 1000);
      });
    }
  

  function findCookieValue(cookieName) {
    var cookieString = document.cookie.split(';').find((a) => a.includes(cookieName)) || '';
    return cookieString !== "" ? cookieString.split('=')[1] : "";
  }

  window.addEventListener('load', function() {
    var _pathname = document.location.pathname;

    if(hr_metrics && hr_metrics.batch_track) hr_metrics.batch_track('PageLoad', _pathname + document.location.search, {
        attribute1: _pathname,
        // check if user is in dark mode or not
        attribute2: findCookieValue('user_theme'),
    });

      if (hr_metrics.track_dwell_time && hr_metrics.set_navigation_data) {
          hr_metrics.track_dwell_time(_pathname);
          hr_metrics.set_navigation_data();
      }

      window.addEventListener('beforeunload', function(){

          var _pathname = document.location.pathname;
          if (hr_metrics){
            if(hr_metrics.batch_track) hr_metrics.batch_track('PageClose', _pathname + document.location.search, {
                attribute2: _pathname
            });
            if(hr_metrics.track_dwell_time) hr_metrics.track_dwell_time(_pathname, true);
            if(hr_metrics.batch_track_record) hr_metrics.batch_track_record(true);
          }
      });

  });
  







  document.addEventListener('click', (e) => {
    const clickableElm = e.target.closest('a[data-analytics], button[data-analytics], input[data-analytics], select[data-analytics], i[data-analytics], div[data-analytics], span[data-analytics], h5[data-analytics]');

    if (clickableElm) {
      if (clickableElm.getAttribute('data-analytics')) {
          action = 'Click'; data = clickableElm.getAttribute('data-analytics');
      } else {
          return;
      }

      
        hr_metrics.batch_track(action, data, (function() {
            var params={};
            for (var _i=1; _i<=12; ++_i){
                var _attr = 'data-attr'+_i;
                if (clickableElm.getAttribute(_attr)){
                  params['attribute'+_i] = clickableElm.getAttribute(_attr);
                }
            }
            var attributes = clickableElm.attributes, attr_length = clickableElm.attributes.length;
            for (var i = 0; i < attr_length; i++){
              var attribute = attributes[i];
              if (attribute.name.indexOf('data-attr-') === 0){
                param_name = attribute.name.substr('data-attr-'.length);
                if (param_name.length > 0) {
                  params[param_name] = attribute.value;
                }
              }
            }
            return params;
        })());
      

      
    }
  }, true);