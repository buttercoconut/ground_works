<template>
  <form @submit.prevent="submitTask">
    <div>
      <label for="depth">Depth (m):</label>
      <input id="depth" v-model="form.depth" type="number" required />
    </div>
    <div>
      <label for="soilLayer">Soil Layer:</label>
      <input id="soilLayer" v-model="form.soilLayer" type="text" required />
    </div>
    <div>
      <label for="location">Location:</label>
      <input id="location" v-model="form.location" type="text" required />
    </div>
    <button type="submit">Submit Task</button>
  </form>
</template>

<script setup>
import { reactive } from 'vue'
import axios from 'axios'

const form = reactive({
  depth: '',
  soilLayer: '',
  location: ''
})

const submitTask = async () => {
  try {
    await axios.post('/api/tasks', form)
    alert('Task submitted successfully')
    form.depth = ''
    form.soilLayer = ''
    form.location = ''
  } catch (e) {
    console.error('Error submitting task', e)
    alert('Failed to submit task')
  }
}
</script>
