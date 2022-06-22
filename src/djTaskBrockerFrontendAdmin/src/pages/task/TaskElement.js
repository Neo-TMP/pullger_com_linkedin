import { paramCase, capitalCase } from 'change-case';
import { useParams, useLocation } from 'react-router-dom';
// @mui
import { Container } from '@mui/material';
// routes
// import { PATH_DASHBOARD } from '../../routes/paths';
// hooks
// import useSettings from '../../hooks/useSettings';
// _mock_
import { _userList } from '../../_mock';
// components
import Page from '../../components/Page';
import HeaderBreadcrumbs from '../../components/HeaderBreadcrumbs';
// sections
import { TaskElementForm } from '../../sections/@dashboard/task/element';

import * as Yup from 'yup';
import { useForm, Controller } from 'react-hook-form';
import { FormProvider } from '../../components/hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
// ----------------------------------------------------------------------

export default function UserCreate() {
  //const { themeStretch } = useSettings();

  const { pathname } = useLocation();

  const { name = '' } = useParams();

  // const isEdit = pathname.includes('edit');
  const isEdit = true;

  const currentUser = _userList.find((user) => paramCase(user.name) === name);
  // const currentUser = '';

  const VerifyCodeSchema = Yup.object().shape({
    code1: Yup.string().required('Code is required'),
    code2: Yup.string().required('Code is required'),
    code3: Yup.string().required('Code is required'),
    code4: Yup.string().required('Code is required'),
    code5: Yup.string().required('Code is required'),
    code6: Yup.string().required('Code is required'),
  });

  const defaultValues = {
    code1: '',
    code2: '',
    code3: '',
    code4: '',
    code5: '',
    code6: '',
  };

  const methods = useForm({
    mode: 'all',
    resolver: yupResolver(VerifyCodeSchema),
    defaultValues,
  });


  return (
    <FormProvider methods={methods}>
      <Page title="User: Create a new user">
        {/*<Container maxWidth={themeStretch ? false : 'lg'}>*/}
        <Container>
          {/*
          <HeaderBreadcrumbs
            heading={!isEdit ? 'Create a new user' : 'Edit user'}
            links={[
              { name: 'Dashboard', href: PATH_DASHBOARD.root },
              { name: 'User', href: PATH_DASHBOARD.user.list },
              { name: !isEdit ? 'New user' : capitalCase(name) },
            ]}
          />
          */}

          <TaskElementForm isEdit={isEdit} currentUser={currentUser} />
        </Container>
      </Page>
    </FormProvider>
  );
 }