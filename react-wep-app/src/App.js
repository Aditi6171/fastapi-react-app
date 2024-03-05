import Employees from './Pages/Employee';
import React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme();

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <Employees />
    </ThemeProvider>
  );
}

// changed by aditi