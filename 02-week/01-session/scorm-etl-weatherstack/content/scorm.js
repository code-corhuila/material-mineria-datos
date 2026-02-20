// SCORM 1.2 Integration for Moodle
// This script handles SCORM communication with the LMS

var scormAPI = {
    isRuntime: function() {
        return typeof(GetInitialize) !== "undefined";
    },
    
    initialize: function() {
        if (this.isRuntime()) {
            try {
                GetInitialize("");
                this.setLessonStatus("incomplete");
                this.setProgressMeasure(0);
            } catch (e) {
                console.log("SCORM: Could not initialize - " + e);
            }
        }
    },
    
    setLessonStatus: function(status) {
        if (this.isRuntime()) {
            try {
                SetValue("cmi.core.lesson_status", status);
                Commit("");
            } catch (e) {
                console.log("SCORM: Could not set lesson status - " + e);
            }
        }
    },
    
    setProgressMeasure: function(value) {
        if (this.isRuntime()) {
            try {
                SetValue("cmi.progress_measure", value);
                Commit("");
            } catch (e) {
                console.log("SCORM: Could not set progress measure - " + e);
            }
        }
    },
    
    setLessonLocation: function(location) {
        if (this.isRuntime()) {
            try {
                SetValue("cmi.core.lesson_location", location);
                Commit("");
            } catch (e) {
                console.log("SCORM: Could not set lesson location - " + e);
            }
        }
    },
    
    finish: function() {
        if (this.isRuntime()) {
            try {
                this.setLessonStatus("completed");
                this.setProgressMeasure(1);
                Commit("");
                GetFinalize("");
            } catch (e) {
                console.log("SCORM: Could not finish - " + e);
            }
        }
    }
};

// Initialize SCORM on page load
document.addEventListener('DOMContentLoaded', function() {
    scormAPI.initialize();
});

// Track scroll progress
var lastScrollPercentage = 0;
window.addEventListener('scroll', function() {
    var scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    var scrollPercentage = scrollHeight > 0 ? window.scrollY / scrollHeight : 0;
    
    if (scrollPercentage >= 0.8 && lastScrollPercentage < 0.8) {
        scormAPI.setProgressMeasure(0.8);
    } else if (scrollPercentage >= 0.5 && lastScrollPercentage < 0.5) {
        scormAPI.setProgressMeasure(0.5);
    }
    
    lastScrollPercentage = scrollPercentage;
    scormAPI.setLessonLocation(window.location.hash || "inicio");
});

// Mark as complete when reaching end
window.addEventListener('scroll', function() {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 100) {
        scormAPI.setLessonStatus("completed");
        scormAPI.setProgressMeasure(1);
    }
});

// Unload handler
window.addEventListener('beforeunload', function() {
    if (scormAPI.isRuntime()) {
        try {
            Commit("");
        } catch (e) {
            console.log("SCORM: Error on unload - " + e);
        }
    }
});
