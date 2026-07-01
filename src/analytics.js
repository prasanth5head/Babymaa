const GA_MEASUREMENT_ID = import.meta.env.VITE_GA_MEASUREMENT_ID || "";

let isAnalyticsInitialized = false;
let isHistoryTrackingEnabled = false;

const loadGoogleAnalyticsScript = () => {
  if (typeof window === "undefined" || !GA_MEASUREMENT_ID || document.getElementById("ga4-script")) {
    return;
  }

  // Google Analytics 4 integration added here.
  const script = document.createElement("script");
  script.id = "ga4-script";
  script.async = true;
  script.src = `https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`;
  document.head.appendChild(script);

  window.dataLayer = window.dataLayer || [];
  window.gtag = function gtag() {
    window.dataLayer.push(arguments);
  };

  window.gtag("js", new Date());
  window.gtag("config", GA_MEASUREMENT_ID, {
    send_page_view: false,
    anonymize_ip: true,
  });
};

export const trackPageView = (path = window.location.pathname + window.location.search) => {
  if (typeof window === "undefined" || !GA_MEASUREMENT_ID || typeof window.gtag !== "function") {
    return;
  }

  // Google Analytics 4 page-view tracking added here.
  window.gtag("event", "page_view", {
    page_path: path,
    page_title: document.title || "Untitled",
  });
};

export const initializeAnalyticsTracking = () => {
  if (isAnalyticsInitialized) {
    return;
  }

  loadGoogleAnalyticsScript();
  trackPageView();

  if (isHistoryTrackingEnabled || !GA_MEASUREMENT_ID) {
    isAnalyticsInitialized = true;
    return;
  }

  const handleHistoryChange = () => {
    trackPageView();
  };

  window.addEventListener("popstate", handleHistoryChange);

  const originalPushState = window.history.pushState;
  window.history.pushState = function patchedPushState(...args) {
    originalPushState.apply(this, args);
    handleHistoryChange();
  };

  const originalReplaceState = window.history.replaceState;
  window.history.replaceState = function patchedReplaceState(...args) {
    originalReplaceState.apply(this, args);
    handleHistoryChange();
  };

  isHistoryTrackingEnabled = true;
  isAnalyticsInitialized = true;
};
