import React from 'react';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import dayjs from 'dayjs';


export default function DatePick(props) {
  console.log(props)
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <DatePicker name={props.name} label={props.label} value={dayjs(props.value)} onChange={props.onChange}/>
    </LocalizationProvider>
  );
}
