<template>
    <section class="section">
        <h3 class="subtitle is-3">
            My Skills
        </h3>
        <div class="columns" id="skillsColumns">
            <div class="column">
                <div
                    class="card animated bounceIn delay-1s"
                    id="frontendCard"
                    hidden
                >
                    <div class="card-content">
                        <div class="content">
                            <h3 class="subtitle is-3">Frontend</h3>
                            <h4 class="subtitle is-5">Languages</h4>
                            <span class="tag">HTML</span>
                            <span class="tag">CSS</span>
                            <span class="tag">Javascript</span>
                            <h4 class="subtitle is-5" style="margin-top: 3%;">
                                Frameworks
                            </h4>
                            <span class="tag">Vue.js</span>
                            <span class="tag">React.js</span>
                            <span class="tag">React Native</span>
                            <span class="tag">Bootstrap</span>
                            <span class="tag">Bulma CSS</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column">
                <div
                    class="card animated bounceIn delay-2s"
                    id="backendCard"
                    hidden
                >
                    <div class="card-content">
                        <div class="content">
                            <h3 class="subtitle is-3">Backend</h3>
                            <h4 class="subtitle is-5">Languages</h4>
                            <span class="tag">Python</span>
                            <span class="tag">Java</span>
                            <span class="tag">Javascript</span>
                            <h4 class="subtitle is-5" style="margin-top: 3%;">
                                Frameworks
                            </h4>
                            <span class="tag">Flask</span>
                            <span class="tag">Spring Boot</span>
                            <span class="tag">Node.js Express</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'Skills',
    methods: {
        handleScroll: function() {
            var rect = document
                .getElementById('skillsColumns')
                .getBoundingClientRect();
            if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
                document
                    .getElementById('frontendCard')
                    .removeAttribute('hidden');
                document
                    .getElementById('backendCard')
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
.section {
    flex-direction: column;
    flex: 1;
}

h3 {
    margin-left: 5%;
}
.tag {
    margin-left: 1%;
    margin-right: 1%;
}
</style>
