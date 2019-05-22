<template v-if="handleScroll">
    <section class="section">
        <h3 class="subtitle is-3 animated fadeInLeft" id="aboutSubtitle">
            About myself
        </h3>
        <p
            class="subtitle is-5 animated fadeInLeftBig delay-1s"
            id="aboutParagraph"
        >
            I'm currently a software engineer working at AT&T. I started my
            career in January 2018 after graduating from college. I graduated
            from the University of Texas at San Antonio with a Bachelor's of
            Science Computer Science in December 2017. I have full stack
            development experience in several languages and frameworks. Check
            out the tech stacks I've used below.
        </p>
    </section>
</template>

<script>
export default {
    name: 'About',
    methods: {
        handleScroll: () => {
            aboutSubtitle.removeAttribute('hidden');
            aboutParagraph.removeAttribute('hidden');
        }
    },
    mounted() {
        document.addEventListener('scroll', this.handleScroll);
        var aboutSubtitle = document.getElementById('aboutSubtitle');
        var aboutParagraph = document.getElementById('aboutParagraph');
        aboutSubtitle.hidden = true;
        aboutParagraph.hidden = true;
        
    }
};
</script>

<style scoped>
p {
    text-align: left;
}
</style>
