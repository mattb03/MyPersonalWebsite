<template>
    <section class="section hero">
        <div class="container" id="contactContainer">
            <h3 class="subtitle is-3">Contact Me</h3>
            <!-- TODO: figure out how to align the name and email boxes with the message box -->
            <div class="columns is-centered">
                <div class="column">
                    <div class="field animated fadeInUp delay-1s" id="nameField" hidden>
                        <label class="label">Name</label>
                        <div class="control">
                            <input type="text" class="input" placeholder="Enter name">
                        </div>
                    </div>
                </div>
                <div class="column">
                    <div class="field animated fadeInUp delay-1s" id="emailField" hidden>
                        <label class="label">Email</label>
                        <div class="control">
                            <input type="text" class="input" placeholder="Enter email">
                        </div>
                    </div>
                </div>
            </div>
            <div class="columns is-centered">
                <div class="column">
                    <div class="field animated fadeInUp delay-1s" id="messageField" hidden>
                        <label class="label">Message</label>
                        <div class="control">
                            <textarea cols="30" rows="10" class="textarea">Enter a message</textarea>
                        </div>
                    </div>
                </div>
            </div>
            <div class="columns is-centered">
                <div class="column is-one-third">
                    <div class="field animated fadeInUp delay-2s" id="submitButtonField" hidden>
                        <div class="control">
                            <button class="button is-rounded" type="submit">Submit</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'Contact',
    methods: {
        handleScroll: function() {
            
            var rect = document.getElementById('contactContainer').getBoundingClientRect();
            if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
                document.getElementById('nameField').removeAttribute('hidden');
                document.getElementById('emailField').removeAttribute('hidden');
                document.getElementById('messageField').removeAttribute('hidden');
                document.getElementById('submitButtonField').removeAttribute('hidden');
            }

        }
    },
    mounted() {
        document.addEventListener('scroll', this.handleScroll);
    }
};
</script>

<style scoped>
@media only screen and (max-width: 769px) {
    button {
        margin-left: 36%;
    }
}
@media only screen and (min-width: 770px) {
    button {
        margin-left: 20%;
    }
}
</style>

