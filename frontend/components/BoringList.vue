<template>
  <div>
    <ul>
      <li v-for="boring in borings" :key="boring.id">
        Depth: {{ boring.depth }}, Compaction: {{ boring.compaction }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
const borings = ref([])

onMounted(async () => {
  const res = await fetch('http://localhost:8000/borings/')
  borings.value = await res.json()
})
</script>
