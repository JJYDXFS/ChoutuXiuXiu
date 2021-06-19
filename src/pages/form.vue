<template>
  <el-row :gutter="20">
    <el-col :xs="24" :md="12">
      <BarChart />
    </el-col>
    <el-col :xs="24" :md="6">
      <DataTable />
    </el-col>
    <el-col :xs="24" :md="6">
      <DataForm />
    </el-col>
  </el-row>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import BarChart from "../components/BarChart.vue";
import DataForm from "../components/DataForm.vue";
import DataTable from "../components/DataTable.vue";

export default defineComponent({
  components: {
    BarChart,
    DataForm,
    DataTable,
  },
});
</script>
