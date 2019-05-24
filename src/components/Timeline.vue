<template>
    <section class="section">
        <h3 class="subtitle is-3">My Timeline</h3>
        <div class="timeline is-centered" id="timelineSection">
            <div class="timeline-item is-primary animated bounceIn" id="timelineItem1">
                <div class="timeline-marker is-primary"></div>
                <div class="timeline-content">
                    <p class="heading">
                        August 2014
                    </p>
                    <p>Started at the University of Texas at San Antonio</p>
                </div>
            </div>
            <div class="timeline-item is-info animated bounceIn delay-1s" id="timelineItem2">
                <div class="timeline-marker is-info">
                </div>
                <div class="timeline-content">
                    <p class="heading">
                        June 2017
                    </p>
                    <p>Began my internship at AT&T as a software engineer</p>
                </div>
            </div>
            <div class="timeline-item is-info animated bounceIn delay-2s" id="timelineItem3">
                <div class="timeline-marker is-info"></div>
                <div class="timeline-content">
                    <p class="heading">August 2017</p>
                    <p>Finished my internship at AT&T</p>
                </div>
            </div>
            <div class="timeline-item is-primary animated bounceIn delay-3s" id="timelineItem4">
                <div class="timeline-marker is-primary"></div>
                <div class="timeline-content">
                    <p class="heading">December 2017</p>
                    <p>Graduated from UTSA with a Bachelor of Science, Computer Science, Cum Laude</p>
                </div>
            </div>
            <div class="timeline-item is-info animated bounceIn delay-4s" id="timelineItem5">
                <div class="timeline-marker is-info"></div>
                <div class="timeline-content">
                    <p class="heading">January 2018</p>
                    <p>Began my career AT&T as a software engineer</p>
                </div>
            </div>
            <div class="timeline-item is-info animated bounceIn delay-5s" id="timelineItem6">
                <div class="timeline-marker is-info"></div>
                <div class="timeline-content">
                    <p class="heading">Present</p>
                    <p>Currently working as a software engineer at AT&T</p>
                </div>
            </div>
        </div>
    </section>
</template>

<script>

export default {
    name: 'Timeline',
    methods: {
        handleScroll: function() {
            var rect = document.getElementById('timelineItem1').getBoundingClientRect();
            if ((rect.top >= 0) && (rect.bottom <= window.innerHeight)) {
                /*
                document.getElementById('timelineItem1').style.display = 'block';
                document.getElementById('timelineItem2').style.display = 'block';
                document.getElementById('timelineItem3').style.display = 'block';
                document.getElementById('timelineItem4').style.display = 'block';
                document.getElementById('timelineItem5').style.display = 'block';
                document.getElementById('timelineItem6').style.display = 'block';
                */
            }
        }
    },
    mounted() {
        document.addEventListener('scroll', this.handleScroll);
        /*
        document.getElementById('timelineItem1').style.display = 'none';
        document.getElementById('timelineItem2').style.display = 'none';
        document.getElementById('timelineItem3').style.display = 'none';
        document.getElementById('timelineItem4').style.display = 'none';
        document.getElementById('timelineItem5').style.display = 'none';
        document.getElementById('timelineItem6').style.display = 'none';
        */
        document.getElementById('timelineSection').hidden = true;

    }
};
</script>
