<template>
    <section class="section">
        <h3 class="subtitle is-3" id="aboutSubtitle" hidden>
            About myself
        </h3>
        <p
            class="subtitle is-5 animated fadeInLeftBig delay-1s"
            id="aboutParagraph"
            hidden
        >
            I'm a software engineer with 17 months professional working experience. I started my
            career in January 2018, after graduating from the University of Texas at San Antonio with a Bachelor's of
            Science, Computer Science in December 2017. I have full stack
            development experience in several languages and frameworks. Check
            out the tech stacks I've used below.
        </p>
    </section>
</template>

<script>
export default {
    name: 'About',
    methods: {
        handleScroll: function() {
            var rect = document
                .getElementById('aboutSubtitle')
                .getBoundingClientRect();
            if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
                document
                    .getElementById('aboutSubtitle')
                    .removeAttribute('hidden');
            }
            rect = document
                .getElementById('aboutParagraph')
                .getBoundingClientRect();
            if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
                document
                    .getElementById('aboutParagraph')
                    .removeAttribute('hidden');
            }
        }
    },
    mounted() {
        document.addEventListener('scroll', this.handleScroll);
    }
};
</script>

<style scoped>
p {
    text-align: left;
}
</style>
